from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import FlatPage


class HomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return ('home'),

    def location(self, obj):
        return reverse(obj)


class FlatPageSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        return FlatPage.objects.all()

    def priority(self, obj):
        return obj.sitemap_priority
