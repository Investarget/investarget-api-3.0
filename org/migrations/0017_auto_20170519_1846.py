# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-19 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0016_auto_20170519_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='orgtransactionphase',
            field=models.ManyToManyField(blank=True, through='org.orgTransactionPhase', to='sourcetype.TransactionPhases'),
        ),
    ]
