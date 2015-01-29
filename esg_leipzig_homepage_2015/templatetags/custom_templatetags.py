import re

from django import template
from django.utils.timezone import now
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active_string(context, flatpage):
    """
    Returns the string ' active' if the requested url starts with the absolute
    url of the given flatpage. Else returns an empty string.
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
    Returns a string with the actual year and the name of the organization.
    """
    return '%d %s' % (
        now().year,
        _('Evangelische Studierendengemeinde Leipzig'))
