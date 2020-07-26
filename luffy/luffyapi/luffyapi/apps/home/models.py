from django.db import models
from utils.models import BaseModel
# Create your models here.


class Banner(BaseModel):
    name = models.CharField(verbose_name='图片', max_length=32)
    img = models.ImageField(upload_to='banner',verbose_name='轮播图',help_text='图片尺寸:3840*800',null=True)
    link = models.CharField(verbose_name='跳转链接',max_length=32)
    info = models.TextField(verbose_name='图片简介')

    def __str__(self):
        return self.name