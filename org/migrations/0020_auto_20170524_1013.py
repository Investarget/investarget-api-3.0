# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-24 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0019_auto_20170523_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='nameC',
            new_name='orgnameC',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='nameE',
            new_name='orgnameE',
        ),
    ]