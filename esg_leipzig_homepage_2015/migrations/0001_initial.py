# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('on_home', models.BooleanField(default=True, verbose_name='Auf der Startseite', help_text='Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.')),
                ('title', models.CharField(max_length=255, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(null=True, max_length=255, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(null=True, max_length=255, verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_de', models.TextField(null=True, blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_en', models.TextField(null=True, blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('begin', models.DateTimeField(verbose_name='Beginn', help_text="Beispiel: '2013-07-20 14:00'.")),
                ('duration', models.PositiveIntegerField(null=True, blank=True, verbose_name='Dauer in Minuten', help_text='Wenn nichts angegeben ist, wird keine Zeit für das Ende der Veranstaltung angezeigt.')),
            ],
            options={
                'verbose_name_plural': 'Veranstaltungen',
                'verbose_name': 'Veranstaltung',
                'ordering': ('begin',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug/URL', help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.")),
                ('title', models.CharField(max_length=100, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(null=True, max_length=100, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(null=True, max_length=100, verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(blank=True, max_length=255, verbose_name='URL zum Titelbild', help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.")),
                ('headline', models.CharField(blank=True, max_length=255, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('headline_de', models.CharField(blank=True, null=True, max_length=255, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('headline_en', models.CharField(blank=True, null=True, max_length=255, verbose_name='Schlagzeile', help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_de', models.TextField(null=True, blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_en', models.TextField(null=True, blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('weight', models.IntegerField(default=100, verbose_name='Platzierung', help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.')),
                ('template_name', models.CharField(blank=True, max_length=255, verbose_name='Vorlage', help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.")),
                ('sitemap_priority', models.DecimalField(max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Priorität in der Sitemap', default=0.5, help_text='Die Zahl gibt die Priorität in der Sitemap an. Sie wird von Suchmaschinen ausgewertet. Siehe <a href="http://www.sitemaps.org/de/protocol.html#prioritydef">Definition im Sitemapprotokoll</a>.', decimal_places=1)),
                ('parent', models.ForeignKey(blank=True, verbose_name='Elternelement', help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht in den Menüs.', to='esg_leipzig_homepage_2015.FlatPage', null=True)),
            ],
            options={
                'verbose_name_plural': 'Statische Seiten',
                'verbose_name': 'Statische Seite',
                'ordering': ('weight', 'slug'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('mediafile', models.FileField(upload_to='', max_length=255, verbose_name='Datei')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Dateien',
                'verbose_name': 'Datei',
                'ordering': ('-uploaded_on',),
            },
            bases=(models.Model,),
        ),
    ]
