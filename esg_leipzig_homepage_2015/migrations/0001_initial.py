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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('on_home', models.BooleanField(verbose_name='Auf der Startseite', default=True, help_text='Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.')),
                ('title', models.CharField(verbose_name='Titel', max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(verbose_name='Titel', max_length=255, null=True, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(verbose_name='Titel', max_length=255, null=True, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_de', models.TextField(blank=True, verbose_name='Inhalt (HTML)', null=True, help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_en', models.TextField(blank=True, verbose_name='Inhalt (HTML)', null=True, help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('begin', models.DateTimeField(verbose_name='Beginn', help_text="Beispiel: '2013-07-20 14:00'.")),
                ('duration', models.PositiveIntegerField(blank=True, verbose_name='Dauer in Minuten', null=True, help_text='Wenn nichts angegeben ist, wird keine Zeit für das Ende der Veranstaltung angezeigt.')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('slug', models.SlugField(verbose_name='Slug/URL', help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.", unique=True)),
                ('title', models.CharField(verbose_name='Titel', max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(verbose_name='Titel', max_length=100, null=True, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(verbose_name='Titel', max_length=100, null=True, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('is_in_navbar', models.BooleanField(verbose_name='In der oberen Navigationsleiste', default=False)),
                ('is_in_main_menu', models.BooleanField(verbose_name='Im rechten Hauptmenü', default=True)),
                ('header_image_url', models.CharField(blank=True, verbose_name='URL zum Titelbild', max_length=255, help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.")),
                ('headline', models.CharField(blank=True, verbose_name='Schlagzeile', max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('headline_de', models.CharField(blank=True, verbose_name='Schlagzeile', max_length=255, null=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('headline_en', models.CharField(blank=True, verbose_name='Schlagzeile', max_length=255, null=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_de', models.TextField(blank=True, verbose_name='Inhalt (HTML)', null=True, help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_en', models.TextField(blank=True, verbose_name='Inhalt (HTML)', null=True, help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('weight', models.IntegerField(verbose_name='Platzierung', default=100, help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.')),
                ('template_name', models.CharField(blank=True, verbose_name='Vorlage', max_length=255, help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.")),
                ('parent', models.ForeignKey(verbose_name='Elternelement', help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht in den Menüs.', blank=True, null=True, to='esg_leipzig_homepage_2015.FlatPage')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mediafile', models.FileField(upload_to='', verbose_name='Datei', max_length=255)),
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
