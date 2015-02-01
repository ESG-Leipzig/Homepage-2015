from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Event, FlatPage, MediaFile


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'begin'
    list_display = ('title', 'begin',)


class FlatPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'weight',)


class MediaFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'uploaded_on'
    list_display = ('mediafile', 'uploaded_on',)


admin.site.register(Event, EventAdmin)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(MediaFile, MediaFileAdmin)
admin.site.unregister(Group)
