# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0003_auto_20170410_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Temperature'), (2, 'Humidity')], default=1),
        ),
    ]
