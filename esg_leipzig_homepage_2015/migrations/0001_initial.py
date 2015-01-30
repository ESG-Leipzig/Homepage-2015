# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel')),
                ('title_de', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('title_en', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('title_fr', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('begin', models.DateTimeField(help_text="Beispiel: '2013-07-20 14:00'.", verbose_name='Beginn')),
                ('duration', models.PositiveIntegerField(help_text='Ein Tag hat 1440 Minuten.', null=True, verbose_name='Dauer in Minuten', blank=True)),
            ],
            options={
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
                'ordering': ('begin',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('slug', models.SlugField(help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.", verbose_name='Slug/URL', unique=True)),
                ('title', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel')),
                ('title_de', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('title_en', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('title_fr', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(max_length=255, help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", verbose_name='URL zum Titelbild', blank=True)),
                ('headline', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile', blank=True)),
                ('headline_de', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('headline_en', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('headline_fr', models.CharField(max_length=255, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile', blank=True)),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)', blank=True)),
                ('weight', models.IntegerField(default=100, verbose_name='Platzierung', help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.')),
                ('template_name', models.CharField(max_length=255, help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", verbose_name='Vorlage', blank=True)),
                ('parent', models.ForeignKey(verbose_name='Elternelement', to='esg_leipzig_homepage_2015.FlatPage', help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht den Menüs.', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Statische Seite',
                'verbose_name_plural': 'Statische Seiten',
                'ordering': ('weight', 'slug'),
            },
            bases=(models.Model,),
        ),
    ]
