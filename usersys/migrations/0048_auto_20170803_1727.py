# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-03 17:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.customClass


class Migration(migrations.Migration):

    dependencies = [
        ('usersys', '0047_myuser_orgarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='IR',
            field=utils.customClass.MyForeignKey(blank=True, help_text='IR', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='ishasfundorplan',
            field=models.TextField(blank=True, default='\u662f\u5426\u6709\u4ea7\u4e1a\u57fa\u91d1\u6216\u6210\u7acb\u8ba1\u5212', help_text='\u662f\u5426\u6709\u4ea7\u4e1a\u57fa\u91d1\u6216\u6210\u7acb\u8ba1\u5212'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mergedynamic',
            field=models.TextField(blank=True, default='\u5e76\u8d2d\u52a8\u6001', help_text='\u5e76\u8d2d\u52a8\u6001'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='targetdemand',
            field=models.TextField(blank=True, default='\u6807\u7684\u9700\u6c42', help_text='\u6807\u7684\u9700\u6c42'),
        ),
    ]