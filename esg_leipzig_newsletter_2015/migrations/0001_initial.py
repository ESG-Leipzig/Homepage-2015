# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=255, verbose_name='Betreff', help_text="Beispiel: 'Newsletter der ESG Leipzig – Wintersemester 2015/2016 – Ausgabe 12'.")),
                ('text', models.TextField(verbose_name='Text', help_text='Der Newsletter wird als plain text versendet, das heißt, HTML-Tags können nicht verwendet werden.')),
                ('mailed_on', models.DateTimeField(auto_now_add=True, verbose_name='Versendet am')),
            ],
            options={
                'verbose_name_plural': 'Ausgaben',
                'verbose_name': 'Ausgabe',
                'ordering': ('mailed_on',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail-Adresse')),
            ],
            options={
                'verbose_name_plural': 'Abonnenten',
                'verbose_name': 'Abonnent',
                'ordering': ('email',),
            },
            bases=(models.Model,),
        ),
    ]
