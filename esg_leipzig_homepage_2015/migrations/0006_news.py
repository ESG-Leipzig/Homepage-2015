# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0005_linktoflatpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Titel', max_length=255, help_text="Beispiel: 'Schrank abzugeben'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_de', models.CharField(null=True, verbose_name='Titel', max_length=255, help_text="Beispiel: 'Schrank abzugeben'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('title_en', models.CharField(null=True, verbose_name='Titel', max_length=255, help_text="Beispiel: 'Schrank abzugeben'. Änderungen sind immer in den Sprachfeldern vorzunehmen.")),
                ('content', models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_de', models.TextField(blank=True, null=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('content_en', models.TextField(blank=True, null=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.')),
                ('author', models.CharField(verbose_name='Autor', max_length=255, help_text="Beispiel: 'Frank Martin'.")),
                ('weight', models.IntegerField(verbose_name='Platzierung', help_text='Eine höhere Zahl bedeutet, dass der Eintrag auf der Startseite weiter unten steht.', default=100)),
            ],
            options={
                'verbose_name_plural': 'Aktuelle Informationen',
                'verbose_name': 'Aktuelle Information',
                'ordering': ('weight', 'title'),
            },
            bases=(models.Model,),
        ),
    ]
