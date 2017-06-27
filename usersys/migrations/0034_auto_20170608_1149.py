# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-08 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersys', '0033_auto_20170605_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('as_investoruser', '\u6295\u8d44\u4eba\u8eab\u4efd'), ('as_traderuser', '\u4ea4\u6613\u5e08\u8eab\u4efd'), ('as_adminuser', '\u7ba1\u7406\u5458\u8eab\u4efd'), ('user_adduser', '\u7528\u6237\u65b0\u589e\u7528\u6237'), ('user_deleteuser', '\u7528\u6237\u5220\u9664\u7528\u6237(obj\u7ea7\u522b)'), ('user_changeuser', '\u7528\u6237\u4fee\u6539\u7528\u6237(obj\u7ea7\u522b)'), ('user_getuser', '\u7528\u6237\u67e5\u770b\u7528\u6237(obj\u7ea7\u522b)'), ('user_getuserlist', '\u7528\u6237\u67e5\u770b\u7528\u6237\u5217\u8868'), ('admin_adduser', '\u7ba1\u7406\u5458\u65b0\u589e\u7528\u6237'), ('admin_deleteuser', '\u7ba1\u7406\u5458\u5220\u9664'), ('admin_changeuser', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237\u57fa\u672c\u4fe1\u606f'), ('admin_getuser', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237'))},
        ),
        migrations.AlterModelOptions(
            name='userrelation',
            options={'permissions': (('admin_adduserrelation', '\u7ba1\u7406\u5458\u5efa\u7acb\u7528\u6237\u8054\u7cfb'), ('admin_changeuserrelation', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237\u8054\u7cfb'), ('admin_deleteuserrelation', '\u7ba1\u7406\u5458\u5220\u9664\u7528\u6237\u8054\u7cfb'), ('admin_getuserrelation', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237\u8054\u7cfb'), ('user_adduserrelation', '\u7528\u6237\u5efa\u7acb\u7528\u6237\u8054\u7cfb'), ('user_changeuserrelation', '\u7528\u6237\u6539\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_deleteuserrelation', '\u7528\u6237\u5220\u9664\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_getuserrelation', '\u7528\u6237\u67e5\u770b\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_getuserrelationlist', '\u7528\u6237\u67e5\u770b\u7528\u6237\u8054\u7cfb\u5217\u8868'))},
        ),
    ]