from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy

from .models import Event, FlatPage, MediaFile


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'begin'
    list_display = ('title', 'begin',)


class FlatPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'weight',)


class MediaFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'uploaded_on'
    list_display = ('mediafile', 'uploaded_on',)

site_instance = admin.site
site_instance.site_title = ugettext_lazy('ESG Leipzig Administration')
site_instance.site_header = ugettext_lazy('ESG Leipzig Administration')

site_instance.register(Event, EventAdmin)
site_instance.register(FlatPage, FlatPageAdmin)
site_instance.register(MediaFile, MediaFileAdmin)
site_instance.unregister(Group)
