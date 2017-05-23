# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0044_auto_20170523_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='document_final_signed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_final_signed', to='applications.Document'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 23, 15, 8, 58, 367070), verbose_name='Date'),
        ),
    ]
