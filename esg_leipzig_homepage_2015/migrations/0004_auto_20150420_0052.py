# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0003_auto_20150405_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='on_home',
        ),
        migrations.AddField(
            model_name='event',
            name='on_home_before_begin',
            field=models.PositiveIntegerField(help_text='Die Veranstaltung erscheint so viele Tage vor Beginn auf der Startseite. Wählen Sie 0, wenn die Veranstaltung nur im Kalender und niemals auf der Startseite erscheinen soll.', verbose_name='Auf der Startseite (in Tagen)', default=30),
            preserve_default=True,
        ),
    ]
