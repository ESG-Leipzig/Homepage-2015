import datetime
import json

from django.conf import settings
from django.http import Http404
from django.utils import timezone
from django.views import generic

from .models import Event, FlatPage, News


class HomeView(generic.ListView):
    """
    View for the first page called 'Home'.
    """
    context_object_name = 'event_list'
    model = Event
    template_name = 'home.html'

    def get_queryset(self):
        """
        Returns a queryset of all future events that should appear on home.
        Uses settings.EVENT_DELAY_IN_MINUTES to determine the range.
        """
        time_to_hide = timezone.now() - datetime.timedelta(
            minutes=settings.EVENT_DELAY_IN_MINUTES)
        queryset = super().get_queryset().filter(begin__gte=time_to_hide)
        result = []
        for event in queryset:
            time_to_show = timezone.now() + datetime.timedelta(
                days=event.on_home_before_begin)
            if event.on_home_before_begin > 0 and event.begin <= time_to_show:
                result.append(event)
        return result

    def get_context_data(self, **context):
        """
        Adds all news to the context.
        """
        news_list = News.objects.all()
        return super().get_context_data(news_list=news_list, **context)


class CalendarView(generic.ListView):
    """
    View for a calendar with all events.
    """
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **context):
        """
        Returns the template context. Adds event data as JSON for use in
        Javascript calendar.
        """
        context = super().get_context_data(**context)
        event_list = []
        for event in context['event_list']:
            event_dict = {
                'title': event.title,
                'start': event.begin.isoformat(),
                'description': event.content,
                'className': event.css_class_name}
            if event.duration:
                event_dict['end'] = event.end.isoformat()
            event_list.append(event_dict)
        context['event_list_json'] = json.dumps(event_list)
        return context


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
        Returns the template context. Adds breadcrumb to it if neccessary.
        """
        context = super().get_context_data(**context)
        parent = context['flatpage'].parent
        if parent is None:
            breadcrumb_list = []
        else:
            breadcrumb_list = [context['flatpage']]
            while parent is not None:
                breadcrumb_list.append(parent)
                parent = parent.parent
            breadcrumb_list.reverse()
        context['breadcrumb_list'] = breadcrumb_list
        return context
