#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from proj.models import project
from usersys.models import MyUser
from sourcetype.models import TransactionStatus, DataSource


class timeline(models.Model):
    id = models.AutoField(primary_key=True)
    proj = models.ForeignKey(project,blank=True,null=True,related_name='proj_timelines')
    investor = models.ForeignKey(MyUser,blank=True,null=True,related_name='investor_timelines')
    supporter = models.ForeignKey(MyUser,blank=True,null=True,related_name='supporter_timelines')
    trader = models.ForeignKey(MyUser,blank=True,null=True,related_name='trader_timelines')
    isClose = models.BooleanField(blank=True,default=False)
    closeDate = models.DateTimeField(blank=True,null=True,)
    contractedServiceTime = models.DateTimeField(blank=True,null=True)
    turnoverTime = models.DateTimeField(blank=True,null=True)
    is_deleted = models.BooleanField(blank=True, default=False)
    deleteduser = models.ForeignKey(MyUser, blank=True, null=True, related_name='userdelete_timelines',on_delete=models.SET_NULL)
    deletedtime = models.DateTimeField(blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    createuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usercreate_timelines',on_delete=models.SET_NULL)
    lastmodifytime = models.DateTimeField(auto_now=True)
    lastmodifyuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usermodify_timelines',on_delete=models.SET_NULL)
    datasource = models.ForeignKey(DataSource, help_text='数据源',default=1)
    class Meta:
        db_table = 'timeline'
        permissions = (
            ('admin_getline','管理员查看时间轴'),
            ('admin_changeline', '管理员修改时间轴'),
            ('admin_deleteline', '管理员删除时间轴'),
            ('admin_addline', '管理员添加时间轴'),

            ('user_addline', '用户添加时间轴'),
            ('user_changeline', '用户修改时间轴(obj级别)'),
            ('user_deleteline','用户删除时间轴(obj级别)'),
        )
    def get_timelinestatu(self):
        return self.timeline_transationStatus.all().filter(isActive=True,is_deleted=False)


class timelineTransationStatu(models.Model):
    id = models.AutoField(primary_key=True)
    timeline = models.ForeignKey(timeline,blank=True,null=True,related_name='timeline_transationStatus')
    transationStatus = models.ForeignKey(TransactionStatus,default=1)
    isActive = models.BooleanField(blank=True,default=False)
    alertCycle = models.SmallIntegerField(blank=True,default=7)
    inDate = models.DateTimeField(blank=True,null=True)
    is_deleted = models.BooleanField(blank=True, default=False)
    deleteduser = models.ForeignKey(MyUser, blank=True, null=True, related_name='userdelete_timelinestatus',on_delete=models.SET_NULL)
    deletedtime = models.DateTimeField(blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    createuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usercreate_timelinestatus',on_delete=models.SET_NULL)
    lastmodifytime = models.DateTimeField(auto_now=True)
    lastmodifyuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usermodify_timelinestatus',on_delete=models.SET_NULL)

    class Meta:
        db_table = 'timelineTransationStatus'

class timelineremark(models.Model):
    id = models.AutoField(primary_key=True)
    timeline = models.ForeignKey(timeline,related_name='timeline_remarks',blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    is_deleted = models.BooleanField(blank=True, default=False)
    deleteduser = models.ForeignKey(MyUser, blank=True, null=True, related_name='userdelete_timelineremarks',on_delete=models.SET_NULL)
    deletedtime = models.DateTimeField(blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    createuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usercreate_timelineremarks',on_delete=models.SET_NULL)
    lastmodifytime = models.DateTimeField(auto_now=True)
    lastmodifyuser = models.ForeignKey(MyUser, blank=True, null=True, related_name='usermodify_timelineremarks', on_delete=models.SET_NULL)
    datasource = models.ForeignKey(DataSource, help_text='数据源',default=1)
    class Meta:
        db_table = 'timelineremarks'
        permissions = (
            ('admin_addlineremark','管理员添加时间轴备注'),
            ('admin_getlineremark', '管理员查看时间轴备注'),
            ('admin_changelineremark', '管理员修改时间轴备注'),
            ('admin_deletelineremark', '管理员删除时间轴备注'),

            ('user_addlineremark', '用户添加时间轴备注（obj级别/相对timeline）'),
            ('user_getlineremark', '用户查看时间轴备注（obj级别/相对timeline）'),
            ('user_changelineremark', '用户修改时间轴备注（obj级别/相对timeline）'),
            ('user_deletelineremark','用户删除时间轴备注（obj级别/相对timeline）'),
        )