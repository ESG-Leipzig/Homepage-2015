# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0002_flatpage_sitemap_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='sitemap_priority',
            field=models.DecimalField(verbose_name='Priorität in der Sitemap', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], decimal_places=1, help_text='Die Zahl gibt die Priorität in der Sitemap an. Sie wird von Suchmaschinen ausgewertet. Siehe <a href="http://www.sitemaps.org/de/protocol.html#prioritydef">Definition im Sitemapprotokoll</a>.', default=0.5, max_digits=2),
            preserve_default=True,
        ),
    ]
