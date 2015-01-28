import re

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, flatpage):
    """
    TODO
    """
    request = context.get('request')
    if request and re.match(flatpage.slug, request.path[1:]):
        result = ' active'
    else:
        result = ''
    return result
