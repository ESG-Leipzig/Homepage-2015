# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='on_home',
            field=models.BooleanField(help_text='Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.', verbose_name='Auf der Startseite', default=True),
            preserve_default=True,
        ),
    ]
