# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-28 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0008_sharetoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharetoken',
            options={'permissions': (('shareproj', '\u5206\u4eab\u9879\u76ee\u6743\u9650'),)},
        ),
    ]
