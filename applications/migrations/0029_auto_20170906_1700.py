# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0028_organisationpending_email_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationpending',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
