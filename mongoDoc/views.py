#coding:utf-8

import traceback

import datetime
import time
# Create your views here.
from django.core.paginator import Paginator, EmptyPage
from mongoengine import Q
from rest_framework import viewsets

from mongoDoc.models import GroupEmailData, IMChatMessages, ProjectData, MergeFinanceData, CompanyCatData
from mongoDoc.serializers import GroupEmailDataSerializer, IMChatMessagesSerializer, ProjectDataSerializer, \
    MergeFinanceDataSerializer, CompanyCatDataSerializer
from utils.customClass import JSONResponse, InvestError
from utils.util import SuccessResponse, InvestErrorResponse, ExceptionResponse, catchexcption, logexcption, \
    loginTokenIsAvailable


class CompanyCatDataView(viewsets.ModelViewSet):
    queryset = CompanyCatData.objects.all()
    serializer_class = CompanyCatDataSerializer

    @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            p_cat_name = request.GET.get('p_cat_name')
            queryset = self.queryset
            if p_cat_name:
                queryset = queryset(p_cat_name__icontains=p_cat_name)
            count = queryset.count()
            serializer = self.serializer_class(queryset,many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

    @loginTokenIsAvailable()
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise InvestError(2001, msg=serializer.error_messages)
            return JSONResponse(SuccessResponse(serializer.data))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))


class MergeFinanceDataView(viewsets.ModelViewSet):
    queryset = MergeFinanceData.objects.all()
    serializer_class = MergeFinanceDataSerializer

    # @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            invsest_with = request.GET.get('invsest_with')
            merger_with = request.GET.get('merger_with')
            com_name = request.GET.get('com_name')
            com_id = request.GET.get('com_id')
            page_size = request.GET.get('page_size')
            page_index = request.GET.get('page_index')  # 从第一页开始
            if not page_size:
                page_size = 10
            if not page_index:
                page_index = 1
            queryset = self.queryset
            sort = request.GET.get('sort')
            if invsest_with:
                queryset = queryset(invsest_with__in=[invsest_with])
            if merger_with:
                queryset = queryset(merger_with__icontains=merger_with)
            if com_name:
                queryset = queryset(com_name__icontains=com_name)
            if com_id:
                queryset = queryset(com_id=com_id)
            if sort not in ['True', 'true', True, 1, 'Yes', 'yes', 'YES', 'TRUE']:
                queryset = queryset.order_by('-date',)
            else:
                queryset = queryset.order_by('date',)
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return JSONResponse(SuccessResponse({'count': 0, 'data': []}))
            serializer = self.serializer_class(queryset,many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

    @loginTokenIsAvailable()
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise InvestError(2001, msg=serializer.error_messages)
            return JSONResponse(SuccessResponse(serializer.data))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

class ProjectDataView(viewsets.ModelViewSet):
    queryset = ProjectData.objects.all()
    serializer_class = ProjectDataSerializer

    # @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            com_name = request.GET.get('com_name')
            com_cat_name = request.GET.get('cat')
            com_sub_cat_name = request.GET.get('sub_cat')
            page_size = request.GET.get('page_size')
            page_index = request.GET.get('page_index')  # 从第一页开始
            if not page_size:
                page_size = 10
            if not page_index:
                page_index = 1
            queryset = self.queryset
            sort = request.GET.get('sort')
            if com_name:
                queryset = queryset(com_name__icontains=com_name)
            if com_cat_name:
                queryset = queryset(com_cat_name=com_cat_name)
            if com_sub_cat_name:
                queryset = queryset(com_sub_cat_name=com_sub_cat_name)
            if sort not in ['True', 'true', True, 1, 'Yes', 'yes', 'YES', 'TRUE']:
                queryset = queryset.order_by('-com_born_date',)
            else:
                queryset = queryset.order_by('com_born_date',)
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return JSONResponse(SuccessResponse({'count': 0, 'data': []}))
            serializer = self.serializer_class(queryset,many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

    @loginTokenIsAvailable()
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise InvestError(2001, msg=serializer.error_messages)
            return JSONResponse(SuccessResponse(serializer.data))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))


class GroupEmailDataView(viewsets.ModelViewSet):
    queryset = GroupEmailData.objects.all()
    serializer_class = GroupEmailDataSerializer

    @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            projtitle = request.GET.get('title')
            page_size = request.GET.get('page_size')
            page_index = request.GET.get('page_index')  # 从第一页开始
            if not page_size:
                page_size = 10
            if not page_index:
                page_index = 1
            queryset = self.queryset
            sort = request.GET.get('sort')
            if projtitle:
                queryset = queryset(projtitle__icontains=projtitle)
            if sort not in ['True', 'true', True, 1, 'Yes', 'yes', 'YES', 'TRUE']:
                queryset = queryset.order_by('-savetime',)
            else:
                queryset = queryset.order_by('savetime',)
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return JSONResponse(SuccessResponse({'count': 0, 'data': []}))
            serializer = self.serializer_class(queryset,many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))


def saveSendEmailDataToMongo(data):
    serializer = GroupEmailDataSerializer(data=data)
    try:
        if serializer.is_valid():
            serializer.save()
        else:
            raise InvestError(2001,msg=serializer.error_messages)
    except Exception:
        logexcption()

def readSendEmailDataFromMongo():
    start = datetime.datetime.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    qs = GroupEmailData.objects.filter(savetime__gt=start)
    return GroupEmailDataSerializer(qs,many=True).data


class IMChatMessagesView(viewsets.ModelViewSet):
    queryset = IMChatMessages.objects.all()
    serializer_class = IMChatMessagesSerializer

    @loginTokenIsAvailable()
    def list(self, request, *args, **kwargs):
        try:
            chatto = request.GET.get('to')
            chatfrom = str(request.user.id)
            page_size = request.GET.get('max_size')
            timestamp = request.GET.get('timestamp')
            if not page_size:
                page_size = 20
            if not timestamp:
                timestamp = int(time.time())*1000
            queryset = self.queryset(timestamp__lt=str(timestamp))
            sort = request.GET.get('sort')
            if chatto:
                queryset = queryset(Q(to=chatto, chatfrom=chatfrom)|Q(to=chatfrom, chatfrom=chatto))
            else:
                queryset = queryset(Q(chatfrom=chatfrom) | Q(to=chatfrom))
            if sort not in ['True', 'true', True, 1, 'Yes', 'yes', 'YES', 'TRUE']:
                queryset = queryset.order_by('-timestamp',)
            else:
                queryset = queryset.order_by('timestamp',)
            count = queryset.count()
            queryset = queryset[0:page_size]
            serializer = self.serializer_class(queryset,many=True)
            return JSONResponse(SuccessResponse({'count':count,'data':serializer.data}))
        except InvestError as err:
            return JSONResponse(InvestErrorResponse(err))
        except Exception:
            catchexcption(request)
            return JSONResponse(ExceptionResponse(traceback.format_exc().split('\n')[-2]))

def saveChatMessageDataToMongo(data):
    queryset = IMChatMessages.objects.all()
    if queryset(msg_id=data['msg_id']).count() > 0:
        pass
    else:
        serializer = IMChatMessagesSerializer(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
            else:
                raise InvestError(2001, msg=serializer.error_messages)
        except Exception:
            logexcption()