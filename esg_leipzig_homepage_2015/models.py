import datetime

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.formats import localize
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy


class FlatPage(models.Model):
    """
    Model for static pages.
    """
    slug = models.SlugField(
        ugettext_lazy('Slug/URL'),
        unique=True,
        help_text=ugettext_lazy(
            "Beispiel: 'impressum'. Jede Seite muss einen individuellen "
            "Eintrag haben."))
    title = models.CharField(
        ugettext_lazy('Titel'),
        max_length=100,
        help_text=ugettext_lazy(
            "Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs "
            "angezeigt. Änderungen sind immer in den Sprachfeldern "
            "vorzunehmen."))
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
            "Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen "
            "sind immer in den Sprachfeldern vorzunehmen."))
    content = models.TextField(
        ugettext_lazy('Inhalt (HTML)'),
        blank=True,
        help_text=ugettext_lazy(
            'Es können alle HTML-Tags verwendet werden. Vergleiche <a href='
            '"https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel'
            '-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. '
            'Änderungen sind immer in den Sprachfeldern vorzunehmen.'))
    parent = models.ForeignKey(
        'self',
        verbose_name=ugettext_lazy('Elternelement'),
        null=True,
        blank=True,
        help_text=ugettext_lazy(
            'Wenn die Seite eine Unterseite sein soll, ist hier das '
            'Elternelement einzutragen. Bleibt das Feld leer, residiert die '
            'Seite auf der obersten Ebene. Unterseiten erscheinen nicht in '
            'den Menüs.'))
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
            "Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches "
            "angegeben ist, wird die Vorlage 'flatpage_default.html' "
            "verwendet."))
    sitemap_priority = models.DecimalField(
        ugettext_lazy('Priorität in der Sitemap'),
        max_digits=2,
        decimal_places=1,
        default=0.5,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text=ugettext_lazy(
            'Die Zahl gibt die Priorität in der Sitemap an. Sie wird von '
            'Suchmaschinen ausgewertet. Siehe '
            '<a href="http://www.sitemaps.org/de/protocol.html#prioritydef">'
            'Definition im Sitemapprotokoll</a>.'))

    class Meta:
        ordering = ('weight', 'slug',)
        verbose_name = ugettext_lazy('Statische Seite')
        verbose_name_plural = ugettext_lazy('Statische Seiten')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to the flatpage. Slugs of child and parent pages are
        combined.
        """
        url = reverse('flatpage', args=[self.slug])
        if self.parent is not None:
            url = self.parent.get_absolute_url()[:-1] + url
        return url

    def clean(self):
        """
        Checks parent field to prevent hierarchical loops.
        """
        super().clean()
        ancestor = self.parent
        while ancestor is not None:
            if ancestor == self:
                raise ValidationError(_(
                    'Fehler: Es darf keine zirkuläre Hierarchie erstellt '
                    'werden. Wählen Sie ein anderes Elternelement.'))
            ancestor = ancestor.parent


class Event(models.Model):
    """
    Model for events that appear in the calendar.
    """
    on_home = models.BooleanField(
        ugettext_lazy('Auf der Startseite'),
        default=True,
        help_text=ugettext_lazy(
            'Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.'))
    title = models.CharField(
        ugettext_lazy('Titel'),
        max_length=255,
        help_text=ugettext_lazy(
            "Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind "
            "immer in den Sprachfeldern vorzunehmen."))
    content = models.TextField(
        ugettext_lazy('Inhalt (HTML)'),
        blank=True,
        help_text=ugettext_lazy(
            'Es können alle HTML-Tags verwendet werden. Änderungen sind immer '
            'in den Sprachfeldern vorzunehmen.'))
    begin = models.DateTimeField(
        ugettext_lazy('Beginn'),
        help_text=ugettext_lazy("Beispiel: '2013-07-20 14:00'."))
    duration = models.PositiveIntegerField(
        ugettext_lazy('Dauer in Minuten'),
        null=True,
        blank=True,
        help_text=ugettext_lazy(
            'Wenn nichts angegeben ist, wird keine Zeit für das Ende der '
            'Veranstaltung angezeigt.'))

    class Meta:
        ordering = ('begin',)
        verbose_name = ugettext_lazy('Veranstaltung')
        verbose_name_plural = ugettext_lazy('Veranstaltungen')

    def __str__(self):
        return ' – '.join((localize(self.begin), self.title))

    @property
    def end(self):
        duration = self.duration or 0
        return self.begin + datetime.timedelta(minutes=duration)


class MediaFile(models.Model):
    """
    Model for uploaded files like images.
    """
    mediafile = models.FileField(
        ugettext_lazy('Datei'),
        max_length=255)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-uploaded_on',)
        verbose_name = ugettext_lazy('Datei')
        verbose_name_plural = ugettext_lazy('Dateien')

    def __str__(self):
        return self.mediafile.url
