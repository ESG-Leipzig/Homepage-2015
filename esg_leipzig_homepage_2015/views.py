import datetime

from django.conf import settings
from django.http import Http404
from django.utils import timezone
from django.views import generic

from .models import Event, FlatPage


class HomeView(generic.ListView):
    """
    View for the first page called 'Home'.
    """
    model = Event
    template_name = 'home.html'

    def get_queryset(self):
        """
        Returns a queryset of all future events. Uses
        settings.EVENT_DELAY_IN_MINUTES to determine the range.
        """
        hiding_time = timezone.now() - datetime.timedelta(
            minutes=settings.EVENT_DELAY_IN_MINUTES)
        return super().get_queryset().filter(begin__gte=hiding_time)


class FlatPageView(generic.DetailView):
    """
    View for static pages.
    """
    model = FlatPage

    def get_object(self, queryset=None):
        """
        Returns the flatpage instance. Raises Http404 if inexistent.
        """
        queryset = queryset or self.get_queryset()
        url = self.kwargs.get('url')
        for flatpage in queryset.filter(slug=url.split('/')[-1]):
            if flatpage.get_absolute_url().strip('/') == url:
                obj = flatpage
                break
        else:
            raise Http404
        return obj

    def get_template_names(self):
        """
        Returns the template names for the view as list. The name
        'flatpage_default.html' is always appended.
        """
        template_names = []
        if self.object.template_name:
            template_names.append(self.object.template_name)
        template_names.append('flatpage_default.html')
        return template_names

    def get_context_data(self, **context):
        """
        Returns the template context. Adds breadcrumb to it.
        """
        context = super().get_context_data(**context)
        parent = context['flatpage'].parent
        breadcrumb_list = [context['flatpage']]
        while parent is not None:
            breadcrumb_list.append(parent)
            parent = parent.parent
        breadcrumb_list.reverse()
        context['breadcrumb_list'] = breadcrumb_list
        return context
