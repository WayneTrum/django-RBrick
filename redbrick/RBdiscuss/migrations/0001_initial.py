# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u56de\u590d\u5185\u5bb9')),
                ('vedio', models.FileField(upload_to=b'', null=True, verbose_name='\u8bdd\u9898\u89c6\u9891', blank=True)),
                ('chan', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u8bdd\u9898\u56de\u590d',
                'verbose_name_plural': '\u8bdd\u9898\u56de\u590d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
                ('reply', models.ForeignKey(verbose_name='\u56de\u590d', to='RBdiscuss.Reply')),
                ('user', models.ForeignKey(verbose_name='\u8bc4\u8bba\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u56de\u590d\u8bc4\u8bba',
                'verbose_name_plural': '\u56de\u590d\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name='\u8bdd\u9898\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u8bdd\u9898\u5185\u5bb9')),
                ('vedio', models.FileField(upload_to=b'', null=True, verbose_name='\u8bdd\u9898\u89c6\u9891', blank=True)),
                ('chan', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='\u53d1\u8d77\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u8bdd\u9898',
                'verbose_name_plural': '\u8bdd\u9898',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topictype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u8bdd\u9898\u540d\u79f0')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
                'ordering': ('addtime',),
                'verbose_name': '\u8bdd\u9898\u7c7b\u578b',
                'verbose_name_plural': '\u8bdd\u9898\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(verbose_name='\u8bdd\u9898', to='RBdiscuss.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(verbose_name='\u56de\u590d\u8005', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
