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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Titel', help_text="Beispiel: 'ESG-Gottesdienst mit Abendmahl'.", max_length=255)),
                ('content', models.TextField(verbose_name='Inhalt (HTML)', blank=True, help_text="Beispiel: '<div></div>'.")),
                ('begin', models.DateTimeField(verbose_name='Beginn', help_text="Beispiel: '2013-07-20 14:00'.")),
                ('duration', models.PositiveIntegerField(verbose_name='Dauer in Minuten', help_text='Ein Tag hat 1440 Minuten.', default=90)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('slug', models.SlugField(verbose_name='Slug/URL', help_text="Beispiel: 'impressum'. Keinen voran- oder nachgestellten Schrägstrich setzen.")),
                ('title', models.CharField(verbose_name='Titel', help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", max_length=100)),
                ('is_in_navbar', models.BooleanField(verbose_name='In der oberen Navigationsleiste', default=False)),
                ('is_in_main_menu', models.BooleanField(verbose_name='Im rechten Hauptmenü', default=True)),
                ('header_image_url', models.CharField(verbose_name='URL zum Titelbild', blank=True, help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", max_length=255)),
                ('headline', models.CharField(verbose_name='Schlagzeile', blank=True, help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", max_length=255)),
                ('content', models.TextField(verbose_name='Inhalt (HTML)', blank=True, help_text="Beispiel: '<div></div>'.")),
                ('weight', models.IntegerField(verbose_name='Platzierung', help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.', default=100)),
                ('template_name', models.CharField(verbose_name='Vorlage', blank=True, help_text="Beispiel: 'meine_seite.html'. Wenn nichts oder etwas Falsches angegeben ist, wird die Vorlage 'flatpage_default.html' verwendet.", max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Statische Seiten',
                'verbose_name': 'Statische Seite',
                'ordering': ('weight', 'slug'),
            },
            bases=(models.Model,),
        ),
    ]
