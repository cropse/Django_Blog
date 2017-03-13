from zinnia.models import Entry
from zinnia.models import Category
from tagging.models import Tag
import datetime
from django import template
# from django.template.defaultfilters import stringfilter


register = template.Library()

@register.simple_tag
def current_time():
    return datetime.datetime.now()

@register.assignment_tag
def tags_list():
    # order by most post used
    tag_set = Tag.objects.usage_for_model(Entry, counts=True, filters=dict(status=2))
    # print(sorted(tag_set, key=lambda li: li.count, reverse=True))
    tag_set = sorted(tag_set, key=lambda li: li.count, reverse=True)
    # there is tag_set in tag.name and tag.count
    return tag_set

@register.assignment_tag
def Category_list():
    return Category.objects.all()
