#coding=utf8

import datetime


# Create your views here.
import traceback

from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.forms.models import model_to_dict
from rest_framework import filters
from rest_framework import viewsets

from emailmanage.models import emailgroupsendlist
from emailmanage.serializers import Emailgroupsendlistserializer, Usergroupsendlistserializer
from mongoDoc.views import saveSendEmailDataToMongo, readSendEmailDataFromMongo
from proj.models import project
from sourcetype.models import Tag, TransactionType, Industry
from third.views.submail import xsendEmail
from usersys.models import MyUser
from utils.customClass import InvestError, JSONResponse
from utils.util import loginTokenIsAvailable, SuccessResponse, InvestErrorResponse, ExceptionResponse, catchexcption, \
    logexcption


#邮件群发模板
Email_project_sign = 'y0dQe4'

#收集邮件群发任务名单
def getAllProjectsNeedToSendMail():
    try:
        proj_qs = project.objects.filter(isSendEmail=True, is_deleted=False)
        saveEmailGroupSendData(proj_qs)
        proj_qs.update(**{'isSendEmail': False})
    except Exception as err:
        print err.message
        logexcption()


def QStoList(qs):
    result_list = []
    for instance in qs:
        if instance[0]:
            resstr = str(instance[0])
            result_list.append(resstr)
    return result_list

def UserQSToList(user_qs):
    result_list = []
    for user in user_qs:
        dic = {}
        for key ,value in user.items():
            dic[key] = value
        result_list.append(dic)
    return result_list



#保存邮件群发任务名单到mongo
def saveEmailGroupSendData(projs):
    for proj in projs:
        tags = proj.project_tags.all().filter(is_deleted=False).values('tag')
        tagsname = Tag.objects.filter(id__in=tags).values_list('nameC')
        industriesname = Industry.objects.filter(industry_projects__proj=proj, is_deleted=False, industry_projects__is_deleted=False).values_list('industryC')
        transactionTypeName = TransactionType.objects.filter(transactionType_projects__proj=proj, is_deleted=False, transactionType_projects__is_deleted=False).values_list('nameC')
        user_qs = Usergroupsendlistserializer(MyUser.objects.filter(tags__in=tags, user_usertags__is_deleted=False,datasource_id=proj.datasource_id).distinct(), many=True).data
        datadic = {
            'projtitle': proj.projtitleC,
            'proj': {
                'id': proj.id,
                'Title': proj.projtitleC,
                'Tags': QStoList(tagsname),
                'Location': proj.country.countryC,
                'Industry': QStoList(industriesname),
                'FAUSD': proj.financeAmount_USD,
                'TransactionType': QStoList(transactionTypeName),
                'B_introducteC' : proj.p_introducteC,
            },
            'datasource': proj.datasource_id,
            'users': UserQSToList(user_qs),
        }
        saveSendEmailDataToMongo(datadic)


#从mongo获取邮件群发任务名单，执行发送任务
def sendEmailToUser():
    mongodatalist = readSendEmailDataFromMongo()
    for data in mongodatalist:
        userlist = data['users']
        projdata = data['proj']
        datasource = data['datasource']
        for user in userlist:
            sendProjEmailToUser(projdata,user,datasource)



#发送邮件
def sendProjEmailToUser(proj,user,datasource):
    emailaddress = user['email']
    data = {
        'proj' : proj['id'],
        'projtitle': proj['Title'],
        'user' : user['id'],
        'username' : user['usernameC'],
        'userEmail' : emailaddress,
        'isRead': False,
        'readtime' : None,
        'isSend' : False,
        'sendtime' : datetime.datetime.now(),
        'errmsg' : None,
        'datasource' : datasource,
    }
    if emailaddress:
        varsdict = {
            'Title': proj['Title'],
            'Location':proj['Location'],
            'Industry': " ".join(proj['Industry']),
            'Tags': " ".join(proj['Tags']),
            'FAUSD': proj['FAUSD'],
            'TransactionType': " ".join(proj['TransactionType']),
            'B_introducteC': proj['B_introducteC'],
        }
        # response = xsendEmail(emailaddress, Email_project_sign, varsdict)
        # if response.get('status'):
        #     data['isSend'] = True
        #     data['sendtime'] = datetime.datetime.now()
        # else:
        #     data['errmsg'] = response
        data['errmsg'] = 'test group send'
    else:
        data['errmsg'] = 'email 缺失'
    emailsend = Emailgroupsendlistserializer(data=data)
    if emailsend.is_valid():
        emailsend.save()
    else:
        logexcption(msg=emailsend.error_messages)

class EmailgroupsendlistView(viewsets.ModelViewSet):
    """
    list:获取邮件发送记录列表
    update:发送已读回执
    """
    filter_backends = (filters.SearchFilter,filters.DjangoFilterBackend)
    queryset = emailgroupsendlist.objects.all()
    filter_fields = ('proj',)
    search_fields = ('datasource','proj','user','isRead','isSend','projtitle','username','userEmail')
    serializer_class = Emailgroupsendlistserializer


    @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            page_size = request.GET.get('page_size')
            page_index = request.GET.get('page_index')  # 从第一页开始
            if not page_size:
                page_size = 10
            if not page_index:
                page_index = 1
            queryset = self.filter_queryset(self.queryset)
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return JSONResponse(SuccessResponse({'count': 0, 'data': []}))
            serializer = Emailgroupsendlistserializer(queryset, many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

    def update(self, request, *args, **kwargs):
        try:
            emailgroupsend = self.get_object()
            with transaction.atomic():
                data = {
                    'isRead':True,
                    'readtime':datetime.datetime.now(),
                }
                emailserializer = Emailgroupsendlistserializer(emailgroupsend, data=data)
                if emailserializer.is_valid():
                    emailserializer.save()
                else:
                    raise InvestError(code=20071,msg='data有误_%s' % emailserializer.errors)
                return JSONResponse(SuccessResponse(emailserializer.data))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))