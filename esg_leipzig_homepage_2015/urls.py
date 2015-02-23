from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from . import sitemaps, views

sitemaps_dict = {
    'home': sitemaps.HomeSitemap,
    'flatpages': sitemaps.FlatPageSitemap}

urlpatterns = patterns(
    '',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^calendar/$',
        views.CalendarView.as_view(),
        name='calendar'),
    url(r'^admin/',
        include(admin.site.urls)),
    url(r'^i18n/',
        include('django.conf.urls.i18n')),
    url(r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps_dict},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^(?P<url>[-\w/]+)/$',
        views.FlatPageView.as_view(),
        name='flatpage'))
