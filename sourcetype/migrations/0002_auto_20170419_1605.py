# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameC', models.CharField(max_length=32)),
                ('nameE', models.CharField(blank=True, max_length=64, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='auditstatus',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='clienttype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='continent',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='currencytype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='favoritetype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='messagetype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='orgtype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='projectstatus',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='specialty',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='titletype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='transactionphases',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='transactionstatus',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='transactiontype',
            old_name='isdeleted',
            new_name='is_deleted',
        ),
    ]