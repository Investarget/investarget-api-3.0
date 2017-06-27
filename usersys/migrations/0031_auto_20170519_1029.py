# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-19 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0010_auto_20170519_1029'),
        ('usersys', '0030_auto_20170517_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='company',
        ),
        migrations.AddField(
            model_name='myuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sourcetype.Country'),
        ),
    ]