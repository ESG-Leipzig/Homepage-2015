# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0003_event_on_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_de',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_en',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='content_fr',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_de',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_en',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_fr',
            field=models.TextField(blank=True, verbose_name='Inhalt (HTML)', help_text='Es können alle HTML-Tags verwendet werden. Vergleiche <a href="https://github.com/ESG-Leipzig/Homepage-2015/wiki/Beispiel-f%C3%BCr-den-Inhalt-einer-statischen-Seite">Beispiel</a>. Änderungen sind immer in den Sprachfeldern vorzunehmen.', null=True),
            preserve_default=True,
        ),
    ]
