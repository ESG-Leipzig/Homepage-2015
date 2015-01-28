from django.db import models
from django.core.urlresolvers import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import ugettext_lazy


class FlatPage(models.Model):
    """
    TODO
    """
    slug = models.CharField(
        ugettext_lazy('Slug'),
        max_length=255,
        db_index=True,
        help_text=ugettext_lazy(''))
    title = models.CharField(
        ugettext_lazy('Titel'),
        max_length=100,
        help_text=ugettext_lazy(''))
    content = models.TextField(
        ugettext_lazy('Inhalt'),
        blank=True,
        help_text=ugettext_lazy(''))
    weight = models.IntegerField(
        ugettext_lazy('Gewicht'),
        default=0,
        help_text=ugettext_lazy(''))
    template_name = models.CharField(
        ugettext_lazy('Vorlage'),
        max_length=70,
        blank=True,
        help_text=ugettext_lazy("Beispiel: 'meine_seite.html'. Wenn nicht anders angegeben wird 'flatpage_default.html' verwendet."))

    class Meta:
        ordering = ('weight', 'slug',)
        verbose_name = ugettext_lazy('Statische Seite')
        verbose_name_plural = ugettext_lazy('Statische Seiten')

    def __str__(self):
        return "%s -- %s" % (self.slug, self.title)

    def get_absolute_url(self):
        # TODO
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug + '/')
