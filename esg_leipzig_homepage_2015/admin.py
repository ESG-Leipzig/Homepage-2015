from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Event, FlatPage


admin.site.register(Event)
admin.site.register(FlatPage)
admin.site.unregister(Group)
