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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('on_home', models.BooleanField(help_text='Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.', default=True, verbose_name='Aut der Startseite')),
                ('title', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=255, verbose_name='Titel')),
                ('title_de', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=255, verbose_name='Titel')),
                ('title_en', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=255, verbose_name='Titel')),
                ('title_fr', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=255, verbose_name='Titel')),
                ('content', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', verbose_name='Inhalt (HTML)')),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('begin', models.DateTimeField(help_text="Beispiel: '2013-07-20 14:00'.", verbose_name='Beginn')),
                ('duration', models.PositiveIntegerField(help_text='Wenn nichts angegeben ist, wird keine Zeit für das Ende der Veranstaltung angezeigt.', blank=True, null=True, verbose_name='Dauer in Minuten')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('slug', models.SlugField(unique=True, help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.", verbose_name='Slug/URL')),
                ('title', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", max_length=100, verbose_name='Titel')),
                ('title_de', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=100, verbose_name='Titel')),
                ('title_en', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=100, verbose_name='Titel')),
                ('title_fr', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", null=True, max_length=100, verbose_name='Titel')),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", blank=True, max_length=255, verbose_name='URL zum Titelbild')),
                ('headline', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", blank=True, max_length=255, verbose_name='Schlagzeile')),
                ('headline_de', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", blank=True, null=True, max_length=255, verbose_name='Schlagzeile')),
                ('headline_en', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", blank=True, null=True, max_length=255, verbose_name='Schlagzeile')),
                ('headline_fr', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.", blank=True, null=True, max_length=255, verbose_name='Schlagzeile')),
                ('content', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', verbose_name='Inhalt (HTML)')),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', blank=True, null=True, verbose_name='Inhalt (HTML)')),
                ('weight', models.IntegerField(help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.', default=100, verbose_name='Platzierung')),
                ('template_name', models.CharField(help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", blank=True, max_length=255, verbose_name='Vorlage')),
                ('parent', models.ForeignKey(blank=True, help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht in den Menüs.', verbose_name='Elternelement', to='esg_leipzig_homepage_2015.FlatPage', null=True)),
            ],
            options={
                'verbose_name_plural': 'Statische Seiten',
                'ordering': ('weight', 'slug'),
                'verbose_name': 'Statische Seite',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mediafile', models.FileField(max_length=255, upload_to='', verbose_name='Datei')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Dateien',
                'ordering': ('-uploaded_on',),
                'verbose_name': 'Datei',
            },
            bases=(models.Model,),
        ),
    ]
