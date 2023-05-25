from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='odd')
def odd(nums):
    # My custom filter
    return [x for x in nums if x % 2 == 1]


@register.filter(name='lower')
@stringfilter
def lower(value):
    return value.lower()
