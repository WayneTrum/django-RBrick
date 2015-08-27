# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Province(models.Model):
  name = models.CharField(max_length=128,verbose_name=u'省份名称')
  addtime = models.DatetimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'省份'
    verbose_name_plural = u'省份'
    ordering = ('addtime',)


class University(models.Model):
  name = models.CharField(max_length=64,verbose_name=u'大学名称')
  addtime = models.DatetimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)
  province = models.ForiegnKey(Province,verbose_name=u'大学省份')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'大学'
    verbose_name_plural = u'大学'
    ordering = ('addtime',)


class Major(models.Model):
  name = models.CharField(max_length=128,verbose_name=u'专业名称')
  addtime = models.DatetimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'学校专业'
    verbose_name_plural = u'学校专业'
    ordering = ('addtime',)


class Education(models.Model):
  userdetail = models.ForiegnKey(Userdetail,verbose_name=u'用户')
  university = models.ForiegnKey(University,verbose_name=u'大学',blank=True,null=True)
  major ＝ models.ForiegnKey(Major,verbose_name=u'专业',blank=True,null=True)
  startyear = models.SmallIntegerField(verbose_name=u'开始年份',blank=True,null=True)
  endyear = models.SmallIntegerField(verbose_name=u'毕业年份',blank=True,null=True)
  addtime = models.DatetimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.userdetail.user.username

  class Meta:
    verbose_name = u'用户学历'
    verbose_name_plural = u'用户学历'
    ordering = ('addtime',)


class Userdetail(models.Model):
  GENDER = (
    (None, ''),
    (True, '男'),
    (False, '女')
  )
  user = models.OneToOneField(User,verbose_name=u'用户',primary_key=True)
  male = models.NullBooleanField(verbose_name=u'性别',choices=GENDER,help_text=u'是为男，否为女',default=None)
  useravatar = models.ImageField(u'头像', upload_to='useravatar', max_length=128, blank=True)
  edu_background = models.ForiegnKey(Education,verbose_name=u'学历信息',blank=True,null=True)
  addtime = models.DatetimeField(auto_now_add=True,verbose_name=u'创建时间',default=datetime.now)

  def __unicode__(self):
    return self.user.username

  class Meta:
    verbose_name = u'用户信息'
    verbose_name_plural = u'用户信息'
    ordering = ('addtime',)
