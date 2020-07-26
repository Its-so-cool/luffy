from rest_framework import serializers
from . import models
import re
from rest_framework.exceptions import ValidationError
from luffyapi.utils.response import APIResponse
class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = models.User
        fields = ['username','password','id']
        extra_kwargs ={
            'password':{'write_only':True},
            'id':{'read_only':True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)

        self.context['username']=user.username
        self.context['token']=token
        return attrs


    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if re.match('^1[3-9][0-9]{9}$',username):
            user = models.User.objects.filter(phone=username).first()
        elif re.match('^.+@.+$',username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()

        if user:

            res = user.check_password(password)
            if res:

                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户名有误')

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class CODEModelSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    class Meta:
        model =models.User
        fields = ['phone','code']

    def validate(self, attrs):
        user=self._get_user(attrs)
        token=self._get_token(user)

        self.context['username']=user
        self.context['token']=token
        return attrs


    def _get_user(self,attrs):
        from django.core.cache import cache
        from luffyapi.settings import const
        phone=attrs.get('phone')
        code=attrs.get('code')
        if not re.match('1[3-9][0-9]{9}',phone):
            return APIResponse(code=0,msg='手机号不合法')
        c_code=cache.get(const.PHONE_KEY % phone)
        user=models.User.objects.filter(phone=phone).first()
        if user:
            if c_code == code:
                return user
            else:
                raise ValidationError('验证码错误')
        else:
            raise ValidationError('用户名不存在')

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
from rest_framework.mixins import CreateModelMixin
from django.core.cache import cache
from luffyapi.settings import const
class RegisterModelSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4,min_length=4,write_only=True)
    class Meta:
        model =models.User
        fields = ['phone', 'code','password']

    def validate(self, attrs):
        phone = attrs.get('phone')
        code =attrs.get('code')
        c_code = cache.get(const.PHONE_KEY % phone)
        m_phone = models.User.objects.filter(phone=phone).first()
        if not m_phone:
            if re.match('1[3-9][0-9]{9}', phone):
                if code == c_code:
                    attrs['username']=phone
                    attrs.pop('code')
                    return attrs
                else:
                    raise ValidationError('验证码错误')
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('手机号已被注册')

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user

