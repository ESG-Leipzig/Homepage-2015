from datetime import timedelta

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils import timezone
from django.utils.translation import ugettext_lazy

from .models import Event, FlatPage, LinkToFlatPage, MediaFile, News


class ComingEventsFilter(admin.SimpleListFilter):
    """
    Special filter class for admin list_filter: See
    https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    """
    title = ugettext_lazy('Beginn der Veranstaltung')
    parameter_name = 'filter'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the
        coded value for the option that will appear in the URL query. The
        second element is the human-readable name for the option that will
        appear in the right sidebar.
        """
        return (
            ('past', ugettext_lazy('In der Vergangenheit')),
            ('future', ugettext_lazy('In der Zukunft')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the
        query string and retrievable via `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value() == 'past':
            return queryset.filter(begin__lte=timezone.now())
        if self.value() == 'future':
            return queryset.filter(begin__gte=timezone.now())


class EventAdminForm(forms.ModelForm):
    """
    Form for new events in the admin. Adds a field for weekly repetitions.

    Attention: We mention all field explicitly. Care of translation fields if
    you change language settings.
    """
    repetitions = forms.IntegerField(
        label=ugettext_lazy('Wiederholungen (in Wochen)'),
        help_text=ugettext_lazy(
            'Die Veranstaltung wird wöchentlich wiederholt und soll deshalb '
            'mehrfach angelegt werden. Wählen Sie 0 für eine einmalige '
            'Veranstaltung.'),
        min_value=0,
        max_value=15,
        initial=0)

    class Meta:
        model = Event
        fields = (
            'title', 'title_de', 'title_en',
            'content', 'content_de', 'content_en',
            'begin',
            'duration',
            'repetitions',
            'on_home_before_begin',
            'css_class_name')


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'begin'
    list_display = ('title', 'begin', 'duration', 'on_home_before_begin',)
    list_filter = (ComingEventsFilter,)

    def get_changeform_initial_data(self, request):
        return {'content': '<p>\n\n</p>'}

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            form = EventAdminForm
        else:
            form = super().get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            for repetition in range(form.cleaned_data['repetitions']):
                obj.pk = None
                obj.begin = obj.begin + timedelta(weeks=1)
                obj.save()


class FlatPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'weight',)

    def get_changeform_initial_data(self, request):
        return {'content': '<div class="row">\n<div class="col-xs-12">'
                           '\n\n</div>\n</div>'}


class LinkToFlatPageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'path', 'flatpage', 'permanent',)


class MediaFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'uploaded_on'
    list_display = ('mediafile', 'uploaded_on', 'mediafile_url',)

    def mediafile_url(self, obj):
        """
        Returns the URL to the uploaded file.
        """
        return obj.mediafile.url
    mediafile_url.short_description = ugettext_lazy('Adresse (URL)')

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


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)

    def get_changeform_initial_data(self, request):
        return {'content': '<p>\n\n</p>'}


site_instance = admin.site
site_instance.site_title = ugettext_lazy('ESG Leipzig Administration')
site_instance.site_header = ugettext_lazy('ESG Leipzig Administration')

site_instance.register(Event, EventAdmin)
site_instance.register(FlatPage, FlatPageAdmin)
site_instance.register(LinkToFlatPage, LinkToFlatPageAdmin)
site_instance.register(MediaFile, MediaFileAdmin)
site_instance.register(News, NewsAdmin)
site_instance.unregister(Group)
