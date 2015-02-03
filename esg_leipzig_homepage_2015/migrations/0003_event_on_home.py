# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0002_mediafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='on_home',
            field=models.BooleanField(verbose_name='Aut der Startseite', help_text='Wenn deaktiviert, erscheint die Veranstaltung nur im Kalender.', default=True),
            preserve_default=True,
        ),
    ]
