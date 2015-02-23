# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='sitemap_priority',
            field=models.DecimalField(decimal_places=1, default=0.5, verbose_name='Priorität in der Sitemap', help_text='Die Zahl gibt die Priorität in der Sitemap an. Sie wird von Suchmaschinen ausgewertet. Siehe <a href="http://www.sitemaps.org/protocol.html#prioritydef">Definition im Sitemapprotokoll</a>.', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], max_digits=2),
            preserve_default=True,
        ),
    ]
