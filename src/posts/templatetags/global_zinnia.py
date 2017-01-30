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
    # order by most used not done yet
    return list(Tag.objects.all())

@register.assignment_tag
def Category_list():
    return Category.objects.all()
