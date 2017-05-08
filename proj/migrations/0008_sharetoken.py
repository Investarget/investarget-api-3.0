# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-28 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0007_auto_20170425_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareToken',
            fields=[
                ('key', models.CharField(help_text='sharetoken', max_length=50, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='CreatedTime')),
                ('is_deleted', models.BooleanField(default=False, help_text='\u662f\u5426\u5df2\u88ab\u5220\u9664')),
                ('proj', models.ForeignKey(help_text='\u9879\u76ee\u7684\u5206\u4eabtoken', on_delete=django.db.models.deletion.CASCADE, related_name='proj_sharetoken', to='proj.project')),
                ('user', models.ForeignKey(help_text='\u7528\u6237\u7684\u5206\u4eabtoken', on_delete=django.db.models.deletion.CASCADE, related_name='user_sharetoken', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sharetoken',
            },
        ),
    ]