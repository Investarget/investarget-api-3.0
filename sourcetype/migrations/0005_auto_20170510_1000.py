# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0004_auto_20170510_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditstatus',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='clienttype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='continent',
            name='continentC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='continent',
            name='continentE',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='country',
            name='bucket',
            field=models.CharField(blank=True, default='image', max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='countryC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='countryE',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='country',
            name='key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='currencytype',
            name='currencyE',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='nameE',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='favoritetype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='industry',
            name='bucket',
            field=models.CharField(blank=True, default='image', max_length=16),
        ),
        migrations.AlterField(
            model_name='industry',
            name='key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orgarea',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orgarea',
            name='nameE',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='orgtype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nameE',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='titletype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transactionphases',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transactionphases',
            name='nameE',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='transactiontype',
            name='nameC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transactiontype',
            name='nameE',
            field=models.CharField(max_length=128),
        ),
    ]
