# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-13 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_auto_20170614_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='createdtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='timelineremark',
            name='createdtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='timelinetransationstatu',
            name='createdtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]