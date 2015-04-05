# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0002_event_css_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='uploaded_on',
            field=models.DateTimeField(verbose_name='Hochgeladen am', auto_now_add=True),
            preserve_default=True,
        ),
    ]
