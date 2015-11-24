# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(help_text="Beispiel: 'Newsletter der ESG – Wintersemester 2015/2016 – Ausgabe 12'.", verbose_name='Betreff', max_length=255)),
                ('text', models.TextField(help_text='Der Newsletter wird als plain text versendet, das heißt, HTML-Tags können nicht verwendet werden.', verbose_name='Text')),
                ('mailed_on', models.DateTimeField(auto_now_add=True, verbose_name='Versendet am')),
            ],
            options={
                'verbose_name': 'Ausgabe',
                'verbose_name_plural': 'Ausgaben',
                'ordering': ('mailed_on',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(verbose_name='E-Mail-Adresse', max_length=254)),
            ],
            options={
                'verbose_name': 'Abonnent',
                'verbose_name_plural': 'Abonnenten',
                'ordering': ('email',),
            },
            bases=(models.Model,),
        ),
    ]
