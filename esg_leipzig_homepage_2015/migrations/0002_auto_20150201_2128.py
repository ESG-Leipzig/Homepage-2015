# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_de',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_en',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_fr',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(verbose_name='Titel', max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title_de',
            field=models.CharField(null=True, verbose_name='Titel', max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Titel', max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title_fr',
            field=models.CharField(null=True, verbose_name='Titel', max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content',
            field=models.TextField(default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_de',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_en',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_fr',
            field=models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='headline',
            field=models.CharField(verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='headline_de',
            field=models.CharField(null=True, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='headline_en',
            field=models.CharField(null=True, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='headline_fr',
            field=models.CharField(null=True, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='parent',
            field=models.ForeignKey(verbose_name='Elternelement', to='esg_leipzig_homepage_2015.FlatPage', null=True, blank=True, help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht in den Menüs.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title',
            field=models.CharField(verbose_name='Titel', max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title_de',
            field=models.CharField(null=True, verbose_name='Titel', max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Titel', max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title_fr',
            field=models.CharField(null=True, verbose_name='Titel', max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen."),
            preserve_default=True,
        ),
    ]
