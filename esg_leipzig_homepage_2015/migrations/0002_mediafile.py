# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('mediafile', models.FileField(verbose_name='Datei', max_length=255, upload_to='')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Datei',
                'verbose_name_plural': 'Dateien',
                'ordering': ('-uploaded_on',),
            },
            bases=(models.Model,),
        ),
    ]
