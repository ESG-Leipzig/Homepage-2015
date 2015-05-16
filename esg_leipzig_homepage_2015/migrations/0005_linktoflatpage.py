# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_leipzig_homepage_2015', '0004_auto_20150420_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkToFlatPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('path', models.CharField(max_length=255, verbose_name='Pfad (relativ zur Startseite)', unique=True, help_text="Beispiel: 'chor/'. Dies bewirkt, dass der Aufruf von ./chor/ relativ zur Startseite zur ausgewählten statischen Seite, zum Beispiel ./arbeitskreise/chor/ weitergeleitet wird. Der abschließende Schrägstrich darf nicht vergessen werden.", validators=[django.core.validators.RegexValidator(message='Nur Buchstaben, Zahlen, Binde-, Schräg- oder Unterstriche sind zulässig. Am Ende muss ein Schrägstrich stehen.', regex='^[-\\w/]+/$')])),
                ('permanent', models.BooleanField(verbose_name='301-Weiterleitung', default=False, help_text='Wenn nicht ausgewählt, wird eine 302-Weiterleitung verwendet.')),
                ('flatpage', models.ForeignKey(help_text='Statische Seite, zu der der Link weiterleiten soll.', to='esg_leipzig_homepage_2015.FlatPage', verbose_name='Statische Seite')),
            ],
            options={
                'verbose_name_plural': 'Links zu statischen Seiten',
                'verbose_name': 'Link zu einer statischen Seite',
                'ordering': ('path',),
            },
            bases=(models.Model,),
        ),
    ]
