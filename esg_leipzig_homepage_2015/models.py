from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy


class FlatPage(models.Model):
    """
    Model for static pages.
    """
    slug = models.SlugField(
        ugettext_lazy('Slug/URL'),
        help_text=ugettext_lazy(
            "Beispiel: 'impressum'. Keinen voran- oder nachgestellten "
            "Schrägstrich setzen."))
    title = models.CharField(
        ugettext_lazy('Titel'),
        max_length=100,
        help_text=ugettext_lazy(
            "Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs "
            "angezeigt."))
    is_in_navbar = models.BooleanField(
        ugettext_lazy('In der oberen Navigationsleiste'),
        blank=True,
        default=False)
    is_in_main_menu = models.BooleanField(
        ugettext_lazy('Im rechten Hauptmenü'),
        blank=True,
        default=True)
    header_image_url = models.CharField(
        ugettext_lazy('URL zum Titelbild'),
        max_length=255,
        blank=True,
        help_text=ugettext_lazy(
            "Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss "
            "manuell auf den Server geladen werden."))
    headline = models.CharField(
        ugettext_lazy('Schlagzeile'),
        max_length=255,
        blank=True,
        help_text=ugettext_lazy(
            "Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. "
            "Die Schlagzeile wird unter dem Titelbild angezeigt."))
    content = models.TextField(
        ugettext_lazy('Inhalt (HTML)'),
        blank=True,
        help_text=ugettext_lazy("Beispiel: '<div></div>'."))
    weight = models.IntegerField(
        ugettext_lazy('Platzierung'),
        default=100,
        help_text=ugettext_lazy(
            'Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter '
            'unten steht.'))
    template_name = models.CharField(
        ugettext_lazy('Vorlage'),
        max_length=255,
        blank=True,
        help_text=ugettext_lazy(
            "Beispiel: 'meine_seite.html'. Wenn nicht anders angegeben wird "
            "die Vorlage 'flatpage_default.html' verwendet."))

    class Meta:
        ordering = ('weight', 'slug',)
        verbose_name = ugettext_lazy('Statische Seite')
        verbose_name_plural = ugettext_lazy('Statische Seiten')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flatpage', args=[self.slug])
