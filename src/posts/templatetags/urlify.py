from urllib.parse import quote_plus
from django import template
# from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
# @stringfilter
def urlify(value):
    return quote_plus(value)