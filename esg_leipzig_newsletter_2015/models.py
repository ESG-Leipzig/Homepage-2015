from django.db import models
from django.utils.formats import localize
from django.utils.translation import ugettext_lazy


class Issue(models.Model):
    """
    Model for newsletter issues.
    """
    subject = models.CharField(
        ugettext_lazy('Betreff'),
        max_length=255,
        help_text=ugettext_lazy(
            "Beispiel: 'Newsletter der ESG Leipzig – Wintersemester "
            "2015/2016 – Ausgabe 12'."))

    text = models.TextField(
        ugettext_lazy('Text'),
        help_text=ugettext_lazy(
            'Der Newsletter wird als plain text versendet, das heißt, '
            'HTML-Tags können nicht verwendet werden.'))

    mailed_on = models.DateTimeField(
        ugettext_lazy('Versendet am'),
        auto_now_add=True)

    class Meta:
        ordering = ('mailed_on',)
        verbose_name = ugettext_lazy('Ausgabe')
        verbose_name_plural = ugettext_lazy('Ausgaben')

    def __str__(self):
        return ' – '.join((localize(self.mailed_on), self.subject))


class Subscriber(models.Model):
    """
    Model for newsletter subscribers.
    """
    email = models.EmailField(
        ugettext_lazy('E-Mail-Adresse'),
        max_length=254)

    class Meta:
        ordering = ('email',)
        verbose_name = ugettext_lazy('Abonnent')
        verbose_name_plural = ugettext_lazy('Abonnenten')

    def __str__(self):
        return self.email
