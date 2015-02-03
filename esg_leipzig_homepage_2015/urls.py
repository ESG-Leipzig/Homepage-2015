from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy

from . import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(ugettext_lazy(r'^kalender/$'),
        views.CalendarView.as_view(),
        name='calendar'),
    url(r'^admin/',
        include(admin.site.urls)),
    url(r'^i18n/',
        include('django.conf.urls.i18n')),
    url(r'^(?P<url>[-\w/]+)/$',
        views.FlatPageView.as_view(),
        name='flatpage'))
