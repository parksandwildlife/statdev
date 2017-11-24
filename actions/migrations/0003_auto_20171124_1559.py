# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-24 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_auto_20170613_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Communicate'), (2, 'Assign'), (3, 'Refer'), (4, 'Issue'), (5, 'Decline'), (6, 'Publish'), (7, 'Lodge'), (8, 'Next Step'), (9, 'Change'), (10, 'Create')], null=True),
        ),
    ]
