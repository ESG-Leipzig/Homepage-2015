# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0002_auto_20150206_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='content_fr',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='content_fr',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='headline_fr',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='title_fr',
        ),
    ]
