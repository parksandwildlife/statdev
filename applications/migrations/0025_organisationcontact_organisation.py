# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20170602_1200'),
        ('applications', '0024_organisationcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationcontact',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Organisation'),
        ),
    ]
