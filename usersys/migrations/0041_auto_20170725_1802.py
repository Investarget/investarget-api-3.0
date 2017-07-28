# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-25 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersys', '0040_auto_20170725_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('user_adduser', '\u7528\u6237\u65b0\u589e\u7528\u6237'), ('user_deleteuser', '\u7528\u6237\u5220\u9664\u7528\u6237(obj\u7ea7\u522b)'), ('user_changeuser', '\u7528\u6237\u4fee\u6539\u7528\u6237(obj\u7ea7\u522b)'), ('user_getuser', '\u7528\u6237\u67e5\u770b\u7528\u6237(obj\u7ea7\u522b)'), ('admin_adduser', '\u7ba1\u7406\u5458\u65b0\u589e\u7528\u6237'), ('admin_deleteuser', '\u7ba1\u7406\u5458\u5220\u9664'), ('admin_changeuser', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237\u57fa\u672c\u4fe1\u606f'), ('admin_getuser', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237'), ('user_addfavorite', '\u7528\u6237\u6dfb\u52a0favorite(obj\u7ea7\u522b\u2014\u2014\u7ed9\u4ea4\u6613\u5e08\u7684)'), ('user_getfavorite', '\u7528\u6237\u67e5\u770bfavorite(obj\u7ea7\u522b\u2014\u2014\u7ed9\u4ea4\u6613\u5e08\u7684)'))},
        ),
        migrations.AlterModelOptions(
            name='userrelation',
            options={'permissions': (('admin_adduserrelation', '\u7ba1\u7406\u5458\u5efa\u7acb\u7528\u6237\u8054\u7cfb'), ('admin_changeuserrelation', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237\u8054\u7cfb'), ('admin_deleteuserrelation', '\u7ba1\u7406\u5458\u5220\u9664\u7528\u6237\u8054\u7cfb'), ('admin_getuserrelation', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237\u8054\u7cfb'), ('user_adduserrelation', '\u7528\u6237\u5efa\u7acb\u7528\u6237\u8054\u7cfb'), ('user_changeuserrelation', '\u7528\u6237\u6539\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_deleteuserrelation', '\u7528\u6237\u5220\u9664\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_getuserrelation', '\u7528\u6237\u67e5\u770b\u7528\u6237\u8054\u7cfb\uff08obj\u7ea7\u522b\uff09'), ('user_getuserrelationlist', '\u7528\u6237\u67e5\u770b\u7528\u6237\u8054\u7cfb\u5217\u8868'))},
        ),
    ]
