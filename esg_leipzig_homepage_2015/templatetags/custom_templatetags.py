import re

from django import template
from django.utils.translation import ugettext as _

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


@register.simple_tag()
def copyright_note():
    """
    TODO
    """
    return '2015 %s' % _('Evangelische Studierendengemeinde Leipzig')
