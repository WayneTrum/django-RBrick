# -*- coding: utf-8 -*-
from django.db import models
from RBuser.models import *
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Topictype(models.Model):
  name = models.CharField(max_length=128,verbose_name=u'话题名称')
  addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'话题类型'
    verbose_name_plural = u'话题类型'
    ordering = ('addtime',)

class Topic(models.Model):
  user = models.ForeignKey(User,verbose_name=u'发起者',)
  title = models.CharField(max_length=512,verbose_name=u'话题标题')
  content = models.TextField(verbose_name=u'话题内容')
  vedio = models.FileField(verbose_name=u'话题视频',blank=True,null=True)
  chan = models.IntegerField(verbose_name=u'点赞',default=0)
  addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.title

  class Meta:
    verbose_name = u'话题'
    verbose_name_plural = u'话题'
    ordering = ('addtime',)


class Reply(models.Model):
  user = models.ForeignKey(User,verbose_name=u'回复者')
  topic = models.ForeignKey(Topic,verbose_name=u'话题')
  content = models.TextField(verbose_name=u'回复内容')
  vedio = models.FileField(verbose_name=u'话题视频',blank=True,null=True)
  chan = models.IntegerField(verbose_name=u'点赞',default=0)
  addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)
  
  def __unicode__(self):
    return self.user.username

  class Meta:
    verbose_name = u'话题回复'
    verbose_name_plural = u'话题回复'
    ordering = ('addtime',)


class Review(models.Model):
  user = models.ForeignKey(User,verbose_name=u'评论者')
  reply = models.ForeignKey(Reply,verbose_name=u'回复')
  content = models.TextField(verbose_name=u'评论内容')
  addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.user.username

  class Meta:
    verbose_name = u'回复评论'
    verbose_name_plural = u'回复评论'
    ordering = ('addtime',)
