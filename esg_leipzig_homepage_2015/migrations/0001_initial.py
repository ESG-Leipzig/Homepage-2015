# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('slug', models.SlugField(help_text="Beispiel: 'impressum'. Keinen voran- oder nachgestellten Schrägstrich setzen.", verbose_name='Slug/URL')),
                ('title', models.CharField(help_text="Beispiel: 'Impressum'. Der Titel wird als Link in den Menüs angezeigt.", max_length=100, verbose_name='Titel')),
                ('is_in_navbar', models.BooleanField(default=False, verbose_name='In der oberen Navigationsleiste')),
                ('is_in_main_menu', models.BooleanField(default=True, verbose_name='Im rechten Hauptmenü')),
                ('header_image_url', models.CharField(help_text="Beispiel: '/static/custom/myimage.jpg'. Die Bilddatei muss manuell auf den Server geladen werden.", blank=True, max_length=255, verbose_name='URL zum Titelbild')),
                ('headline', models.CharField(help_text="Beispiel: 'Wir feiern gemeinsam Gottesdienste und Andachten.'. Die Schlagzeile wird unter dem Titelbild angezeigt.", blank=True, max_length=255, verbose_name='Schlagzeile')),
                ('content', models.TextField(help_text="Beispiel: '<div></div>'.", blank=True, verbose_name='Inhalt (HTML)')),
                ('weight', models.IntegerField(help_text='Eine höhere Zahl bedeutet, dass der Eintrag im Menü weiter unten steht.', default=100, verbose_name='Platzierung')),
                ('template_name', models.CharField(help_text="Beispiel: 'meine_seite.html'. Wenn nicht anders angegeben wird die Vorlage 'flatpage_default.html' verwendet.", blank=True, max_length=255, verbose_name='Vorlage')),
            ],
            options={
                'verbose_name_plural': 'Statische Seiten',
                'ordering': ('weight', 'slug'),
                'verbose_name': 'Statische Seite',
            },
            bases=(models.Model,),
        ),
    ]
