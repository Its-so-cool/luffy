from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from . import models
from .serializers import BannerModelSerializer
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache
# class BannerView(GenericAPIView,ListModelMixin):
class BannerView(GenericViewSet,ListModelMixin):
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = BannerModelSerializer

    def list(self, request, *args, **kwargs):
        bannerl_list=cache.get('banner_list')
        # print(bannerl_list)
        response=super().list(request, *args, **kwargs)
        if not bannerl_list:
            cache.set('banner_list',response.data,60*60*24)
            return response
        return Response(data=bannerl_list)
