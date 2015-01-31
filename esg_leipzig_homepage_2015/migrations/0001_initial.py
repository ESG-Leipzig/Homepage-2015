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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel', max_length=255)),
                ('title_de', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel', max_length=255, null=True)),
                ('title_en', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel', max_length=255, null=True)),
                ('title_fr', models.CharField(help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", verbose_name='Titel', max_length=255, null=True)),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('begin', models.DateTimeField(help_text="Beispiel: '2013-07-20 14:00'.", verbose_name='Beginn')),
                ('duration', models.PositiveIntegerField(help_text='Wenn nichts angegeben ist, wird keine Zeit für das Ende der Veranstaltung angezeigt.', verbose_name='Dauer in Minuten', blank=True, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text="Beispiel: 'impressum'. Jede Seite muss einen individuellen Eintrag haben.", verbose_name='Slug/URL', unique=True)),
                ('title', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel', max_length=100)),
                ('title_de', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel', max_length=100, null=True)),
                ('title_en', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel', max_length=100, null=True)),
                ('title_fr', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", verbose_name='Titel', max_length=100, null=True)),
                ('is_in_navbar', models.BooleanField(verbose_name='In der oberen Navigationsleiste', default=False)),
                ('is_in_main_menu', models.BooleanField(verbose_name='Im rechten Hauptmenü', default=True)),
                ('header_image_url', models.CharField(help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", verbose_name='URL zum Titelbild', blank=True, max_length=255)),
                ('headline', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile', blank=True, max_length=255)),
                ('headline_de', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile', blank=True, max_length=255, null=True)),
                ('headline_en', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile', blank=True, max_length=255, null=True)),
                ('headline_fr', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", verbose_name='Schlagzeile', blank=True, max_length=255, null=True)),
                ('content', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>.', verbose_name='Inhalt (HTML)', blank=True)),
                ('content_de', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('content_en', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('content_fr', models.TextField(help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>.', verbose_name='Inhalt (HTML)', blank=True, null=True)),
                ('weight', models.IntegerField(help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.', verbose_name='Platzierung', default=100)),
                ('template_name', models.CharField(help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", verbose_name='Vorlage', blank=True, max_length=255)),
                ('parent', models.ForeignKey(null=True, verbose_name='Elternelement', help_text='Wenn die Seite eine Unterseite sein soll, ist hier das Elternelement einzutragen. Bleibt das Feld leer, residiert die Seite auf der obersten Ebene. Unterseiten erscheinen nicht den Menüs.', blank=True, to='esg_leipzig_homepage_2015.FlatPage')),
            ],
            options={
                'verbose_name': 'Statische Seite',
                'verbose_name_plural': 'Statische Seiten',
                'ordering': ('weight', 'slug'),
            },
            bases=(models.Model,),
        ),
    ]
