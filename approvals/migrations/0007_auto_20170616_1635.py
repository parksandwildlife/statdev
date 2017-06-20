# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-16 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0006_auto_20170612_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='app_type',
            field=models.IntegerField(choices=[(1, 'Permit'), (2, 'Licence/permit'), (3, 'Part 5 - New Application'), (4, 'Emergency works'), (5, 'Part 5 - Amendment Request'), (6, 'Part 5 - Amendment Application'), (7, 'Test - Application'), (8, 'Amend Permit'), (9, 'Amend Licence'), (10, 'Renew Permit'), (11, 'Renew Licence')]),
        ),
    ]
