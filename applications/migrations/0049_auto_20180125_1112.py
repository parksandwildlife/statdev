# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-25 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0048_auto_20180123_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='route_status',
            field=models.CharField(blank=True, default='Draft', max_length=256, null=True),
        ),
    ]
