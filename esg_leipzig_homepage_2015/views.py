import datetime

from django.conf import settings
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
        hiding_time = timezone.now() - datetime.timedelta(
            minutes=settings.EVENT_DELAY_IN_MINUTES)
        return super().get_queryset().filter(begin__gte=hiding_time)


class FlatPageView(generic.DetailView):
    """
    View for static pages.
    """
    model = FlatPage

    def get_template_names(self):
        template_names = []
        if self.object.template_name:
            template_names.append(self.object.template_name)
        template_names.append('flatpage_default.html')
        return template_names
