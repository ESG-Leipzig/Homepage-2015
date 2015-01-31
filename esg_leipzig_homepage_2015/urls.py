from django.conf.urls import include, patterns, url
from django.contrib import admin

from . import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^admin/',
        include(admin.site.urls)),
    url(r'^i18n/',
        include('django.conf.urls.i18n')),
    url(r'^(?P<url>[\w/]+)/$',
        views.FlatPageView.as_view(),
        name='flatpage'))
