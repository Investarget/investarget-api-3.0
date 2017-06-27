# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-10 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0005_auto_20170510_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='isPindustry',
            field=models.BooleanField(default=False, help_text='\u662f\u5426\u662f\u7236\u7ea7\u884c\u4e1a'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='Pindustry',
            field=models.ForeignKey(blank=True, help_text='\u7236\u7ea7\u884c\u4e1a', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pindustry_Sindustries', to='sourcetype.Industry'),
        ),
    ]