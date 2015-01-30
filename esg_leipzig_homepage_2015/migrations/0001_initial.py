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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel')),
                ('title_de', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('title_en', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('title_fr', models.CharField(max_length=255, help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", null=True, verbose_name='Titel')),
                ('content', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)')),
                ('content_de', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('content_en', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('content_fr', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('begin', models.DateTimeField(help_text="Beispiel: '2013-07-20 14:00'.", verbose_name='Beginn')),
                ('duration', models.PositiveIntegerField(blank=True, help_text='Ein Tag hat 1440 Minuten.', null=True, verbose_name='Dauer in Minuten')),
            ],
            options={
                'ordering': ('begin',),
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(help_text="Beispiel: 'impressum'. Keinen voran- oder nachgestellten Schrägstrich setzen.", verbose_name='Slug/URL')),
                ('title', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel')),
                ('title_de', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('title_en', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('title_fr', models.CharField(max_length=100, help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", null=True, verbose_name='Titel')),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(max_length=255, blank=True, help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", verbose_name='URL zum Titelbild')),
                ('headline', models.CharField(max_length=255, blank=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile')),
                ('headline_de', models.CharField(max_length=255, blank=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile')),
                ('headline_en', models.CharField(max_length=255, blank=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile')),
                ('headline_fr', models.CharField(max_length=255, blank=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", null=True, verbose_name='Schlagzeile')),
                ('content', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)')),
                ('content_de', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('content_en', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('content_fr', models.TextField(blank=True, help_text='Es können alle HTML-Tags verwendet werden.', null=True, verbose_name='Inhalt (HTML)')),
                ('weight', models.IntegerField(help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.', default=100, verbose_name='Platzierung')),
                ('template_name', models.CharField(max_length=255, blank=True, help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", verbose_name='Vorlage')),
            ],
            options={
                'ordering': ('weight', 'slug'),
                'verbose_name': 'Statische Seite',
                'verbose_name_plural': 'Statische Seiten',
            },
            bases=(models.Model,),
        ),
    ]
