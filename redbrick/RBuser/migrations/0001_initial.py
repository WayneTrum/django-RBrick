# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startyear', models.SmallIntegerField(null=True, verbose_name='\u5f00\u59cb\u5e74\u4efd', blank=True)),
                ('endyear', models.SmallIntegerField(null=True, verbose_name='\u6bd5\u4e1a\u5e74\u4efd', blank=True)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u7528\u6237\u5b66\u5386',
                'verbose_name_plural': '\u7528\u6237\u5b66\u5386',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u4e13\u4e1a\u540d\u79f0')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u5b66\u6821\u4e13\u4e1a',
                'verbose_name_plural': '\u5b66\u6821\u4e13\u4e1a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u7701\u4efd\u540d\u79f0')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u7701\u4efd',
                'verbose_name_plural': '\u7701\u4efd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5927\u5b66\u540d\u79f0')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
                ('province', models.ForeignKey(verbose_name='\u5927\u5b66\u7701\u4efd', to='RBuser.Province')),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u5927\u5b66',
                'verbose_name_plural': '\u5927\u5b66',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
                ('male', models.NullBooleanField(default=None, choices=[(None, b''), (True, b'\xe7\x94\xb7'), (False, b'\xe5\xa5\xb3')], help_text='\u662f\u4e3a\u7537\uff0c\u5426\u4e3a\u5973', verbose_name='\u6027\u522b')),
                ('useravatar', models.ImageField(upload_to=b'useravatar', max_length=128, verbose_name='\u5934\u50cf', blank=True)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.ForeignKey(verbose_name='\u4e13\u4e1a', blank=True, to='RBuser.Major', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='university',
            field=models.ForeignKey(verbose_name='\u5927\u5b66', blank=True, to='RBuser.University', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='userdetail',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to='RBuser.Userdetail'),
            preserve_default=True,
        ),
    ]
