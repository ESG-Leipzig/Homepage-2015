from django.contrib import admin
from django.contrib.auth.models import Group

from .models import FlatPage

admin.site.register(FlatPage)
admin.site.unregister(Group)
