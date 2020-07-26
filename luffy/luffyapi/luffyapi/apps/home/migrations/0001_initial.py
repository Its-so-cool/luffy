# Generated by Django 2.2.2 on 2020-07-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('display_order', models.IntegerField()),
                ('name', models.CharField(max_length=32, verbose_name='图片')),
                ('img', models.ImageField(help_text='图片尺寸:3840*800', null=True, upload_to='banner', verbose_name='轮播图')),
                ('link', models.CharField(max_length=32, verbose_name='跳转链接')),
                ('info', models.TextField(verbose_name='图片简介')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
