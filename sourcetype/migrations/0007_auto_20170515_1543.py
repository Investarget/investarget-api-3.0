# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-15 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0006_auto_20170510_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='industryE',
            field=models.CharField(max_length=128),
        ),
    ]
