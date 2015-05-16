from django.core.urlresolvers import reverse
from django.http import (
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect
)

from .models import LinkToFlatPage


class LinkToFlatPageMiddleware():
    """
    Middleware to check extra links to static pages (see
    models.LinkToFlatPage). If the reponse is an HttpResponseNotFound
    instance the request path is checked against all model instances to see
    whether to change to an HttpResponseRedirect.
    """
    def process_response(self, request, response):
        if not isinstance(response, HttpResponseNotFound):
            result = response
        else:
            path = request.path.lstrip(reverse('home'))
            try:
                link = LinkToFlatPage.objects.get(path=path)
            except LinkToFlatPage.DoesNotExist:
                result = response
            else:
                if link.permanent:
                    result = HttpResponsePermanentRedirect(
                        link.flatpage.get_absolute_url())
                else:
                    result = HttpResponseRedirect(
                        link.flatpage.get_absolute_url())
        return result
