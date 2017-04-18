# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-18 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersys', '0006_auto_20170417_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('as_investoruser', '\u6295\u8d44\u4eba\u8eab\u4efd'), ('as_traderuser', '\u4ea4\u6613\u5e08\u8eab\u4efd'), ('as_supporteruser', '\u9879\u76ee\u65b9\u8eab\u4efd'), ('as_adminuser', '\u7ba1\u7406\u5458\u8eab\u4efd'), ('user_adduser', '\u7528\u6237\u65b0\u589e\u7528\u6237'), ('user_deleteuser', '\u7528\u6237\u5220\u9664\u7528\u6237(obj\u7ea7\u522b\u6743\u9650)'), ('user_changeuser', '\u7528\u6237\u4fee\u6539\u7528\u6237(obj\u7ea7\u522b\u6743\u9650)'), ('user_getuser', '\u7528\u6237\u67e5\u770b\u7528\u6237(obj/class\u7ea7\u522b\u6743\u9650)'), ('admin_adduser', '\u7ba1\u7406\u5458\u65b0\u589e\u7528\u6237'), ('admin_deleteuser', '\u7ba1\u7406\u5458\u5220\u9664'), ('admin_changeuser', '\u7ba1\u7406\u5458\u4fee\u6539\u7528\u6237(\u5305\u542b\u91cd\u7f6e\u5bc6\u7801)'), ('admin_getuser', '\u7ba1\u7406\u5458\u67e5\u770b\u7528\u6237'))},
        ),
        migrations.AlterField(
            model_name='mytoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='CreatedTime'),
        ),
        migrations.AlterField(
            model_name='mytoken',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='\u662f\u5426\u5df2\u88ab\u5220\u9664'),
        ),
    ]
