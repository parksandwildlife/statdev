# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:58
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('upload', models.FileField(max_length=512, upload_to='uploads/%Y/%m/%d')),
                ('name', models.CharField(max_length=256)),
                ('category', models.IntegerField(blank=True, choices=[(1, 'Landowner consent'), (2, 'Deed'), (3, 'Assessment report'), (4, 'Referee response')], null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('text_content', models.TextField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applications.Application'),
        ),
        migrations.AlterField(
            model_name='task',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applications.Application'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ongoing'), (2, 'Complete'), (3, 'Cancelled')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.IntegerField(choices=[(1, 'Assess an application'), (2, 'Refer an application for comment'), (3, 'Assess compliance with a condition')]),
        ),
        migrations.AddField(
            model_name='application',
            name='documents',
            field=models.ManyToManyField(blank=True, to='applications.Document'),
        ),
        migrations.AddField(
            model_name='condition',
            name='documents',
            field=models.ManyToManyField(blank=True, to='applications.Document'),
        ),
        migrations.AddField(
            model_name='location',
            name='documents',
            field=models.ManyToManyField(blank=True, to='applications.Document'),
        ),
        migrations.AddField(
            model_name='task',
            name='documents',
            field=models.ManyToManyField(blank=True, to='applications.Document'),
        ),
    ]
