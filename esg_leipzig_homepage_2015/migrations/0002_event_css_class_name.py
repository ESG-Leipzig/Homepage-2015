# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='css_class_name',
            field=models.CharField(choices=[('event-default', 'Grau'), ('event-primary', 'Dunkelblau'), ('event-success', 'Grün'), ('event-info', 'Hellblau'), ('event-warning', 'Gelb'), ('event-danger', 'Rot')], help_text='Die Farben entsprechen den Farben für Buttons, Labels usw. bei Twitter Bootstrap.', default='event-primary', verbose_name='Farbe', max_length=255),
            preserve_default=True,
        ),
    ]
