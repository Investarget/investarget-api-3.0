# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-05 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetype', '0003_orgarea_namee'),
        ('usersys', '0020_auto_20170505_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfriendship',
            options={'permissions': (('admin_addfriend', '\u7ba1\u7406\u5458\u5efa\u7acb\u7528\u6237\u597d\u53cb\u5173\u7cfb'), ('admin_changefriend', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237\u597d\u53cb\u5173\u7cfb'), ('admin_deletefriend', '\u7ba1\u7406\u5458\u5220\u9664\u7528\u6237\u597d\u53cb\u5173\u7cfb'), ('admin_getfriend', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237\u597d\u53cb\u5173\u7cfb'))},
        ),
        migrations.AddField(
            model_name='userfriendship',
            name='datasource',
            field=models.ForeignKey(default=1, help_text='\u6570\u636e\u6e90', on_delete=django.db.models.deletion.CASCADE, to='sourcetype.DataSource'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfriendship',
            name='friendallowgetfavoriteproj',
            field=models.BooleanField(default=True, help_text='\u63a5\u6536\u4eba\u5141\u8bb8\u597d\u53cb\u67e5\u770b\u81ea\u5df1\u7684\u9879\u76ee\u6536\u85cf'),
        ),
        migrations.AddField(
            model_name='userfriendship',
            name='userallowgetfavoriteproj',
            field=models.BooleanField(default=True, help_text='\u53d1\u8d77\u4eba\u5141\u8bb8\u597d\u53cb\u67e5\u770b\u81ea\u5df1\u7684\u9879\u76ee\u6536\u85cf'),
        ),
        migrations.AlterField(
            model_name='userfriendship',
            name='friend',
            field=models.ForeignKey(help_text='\u63a5\u6536\u4eba', on_delete=django.db.models.deletion.CASCADE, related_name='friend_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfriendship',
            name='user',
            field=models.ForeignKey(help_text='\u53d1\u8d77\u4eba', on_delete=django.db.models.deletion.CASCADE, related_name='user_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]