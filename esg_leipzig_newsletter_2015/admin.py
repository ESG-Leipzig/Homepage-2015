from django.contrib import admin

from .models import Issue, Subscriber


class IssueAdmin(admin.ModelAdmin):
    date_hierarchy = 'mailed_on'
    list_display = ('subject', 'mailed_on',)

    def has_change_permission(self, request, obj=None):
        """
        Returns the default value (True) if obj is None else False. This
        indicates editing of objects of this type is permitted in general
        but not for (every) specific object. This way we get the admin list
        view but not the update (change) views.
        """
        if obj is not None:
            return False
        return super().has_change_permission(request, obj)


class SubscriberAdmin(admin.ModelAdmin):
    list_per_page = 500


admin.site.register(Issue, IssueAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
