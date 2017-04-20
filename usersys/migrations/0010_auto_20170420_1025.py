# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-20 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usersys', '0009_userrelation_datasource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertags',
            name='createdtime',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usertags',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_tags', to='sourcetype.Tag'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertags',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
