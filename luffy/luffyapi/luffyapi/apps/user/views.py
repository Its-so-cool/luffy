from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from . import models
from . import serializers
from rest_framework.decorators import action
from luffyapi.utils.response import APIResponse
from rest_framework.request import Request
import re

# Create your views here.


class LoginModelViewSet (ViewSet):

    @action(methods=['post'],detail=False)
    def login(self,request,*args,**kwargs):
        ser = serializers.UserModelSerializer(data= request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['username']

            return APIResponse(token=token,username=username)

        else:
            return APIResponse(code=0,msg=ser.errors)

    @action(methods=['get'],detail=False)
    def check_telephone(self,request,*args,**kwargs):

        phone=request.query_params.get('phone')

        if not re.match('1[3-9][0-9]{9}',phone):
            return APIResponse(code=0,msg='手机号不合法')
        try:
            models.User.objects.get(phone=phone)

            return APIResponse(code=1)
        except:
            return APIResponse(code=0,msg='手机号不存在')

    @action(methods=['post'], detail=False)
    def code_login(self,request,*args,**kwargs):
        ser = serializers.CODEModelSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['username'].username

            return APIResponse(token=token, username=username)

        else:
            return APIResponse(code=0, msg=ser.errors)



from .throtting import SMSThrotting
class Phone_Throtting(ViewSet):
    throttle_classes = (SMSThrotting,)
    @action(methods=['post'], detail=False)
    def send_phone(self, request, *args, **kwargs):
        from luffyapi.libs.tx_sms import get_code, send
        from django.core.cache import cache
        from luffyapi.settings import const
        phone = request.data.get('phone')
        if not re.match('1[3-9][0-9]{9}', phone):
            return APIResponse(code=0, msg='手机号不合法')
        code = get_code()
        print(code)
        res = send(phone, code)
        # res =1
        #'sms_code_%s'% phone
        cache.set(const.PHONE_KEY % phone, code, 300)
        if res:
            return APIResponse(code=1, msg="发送成功")
        else:
            return APIResponse(code=0, msg='发送失败')

from rest_framework.generics import GenericAPIView
class UserRegister(GenericAPIView):
    serializer_class = serializers.RegisterModelSerializer
    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return APIResponse(code=1,msg='注册成功')
        else:
            return APIResponse(code=0,msg=ser.errors)
from rest_framework.mixins import CreateModelMixin







