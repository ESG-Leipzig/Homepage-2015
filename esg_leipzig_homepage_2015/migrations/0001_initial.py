# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(max_length=255, null=True, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_fr', models.CharField(max_length=255, null=True, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<p>\n\n</p>', verbose_name='Inhalt (HTML)', blank=True)),
                ('begin', models.DateTimeField(verbose_name='Beginn', help_text="Beispiel: '2013-07-20 14:00'.")),
                ('duration', models.PositiveIntegerField(help_text='Wenn nichts angegeben ist, wird keine Zeit für das Ende der Veranstaltung angezeigt.', null=True, verbose_name='Dauer in Minuten', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Veranstaltungen',
                'ordering': ('begin',),
                'verbose_name': 'Veranstaltung',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.", verbose_name='Slug/URL')),
                ('title', models.CharField(max_length=100, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(max_length=100, null=True, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_fr', models.CharField(max_length=100, null=True, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(max_length=255, help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", verbose_name='URL zum Titelbild', blank=True)),
                ('headline', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", verbose_name='Schlagzeile', blank=True)),
                ('headline_de', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('headline_en', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('headline_fr', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True, default='<div class="row">\n<div class="col-xs-12">\n\n</div>\n</div>', verbose_name='Inhalt (HTML)', blank=True)),
                ('weight', models.IntegerField(default=100, verbose_name='Platzierung', help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.')),
                ('template_name', models.CharField(max_length=255, help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", verbose_name='Vorlage', blank=True)),
                ('parent', models.ForeignKey(null=True, help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht in den Menüs.', blank=True, to='esg_leipzig_homepage_2015.FlatPage', verbose_name='Elternelement')),
            ],
            options={
                'verbose_name_plural': 'Statische Seiten',
                'ordering': ('weight', 'slug'),
                'verbose_name': 'Statische Seite',
            },
            bases=(models.Model,),
        ),
    ]
