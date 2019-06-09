#coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='')
    gender = models.CharField(max_length=10,choices=(('males',u'男'),('female',u'女')),verbose_name=u'性别',default='female')
    address = models.CharField(max_length=100,verbose_name=u'地址',default=u'')
    phonenumber = models.CharField(max_length=11,blank=True,default=u'')

    class Meta:
        '''
        后台展示名称
        '''
        verbose_name_plural = verbose_name = u'账户信息'


    def __unicode__(self):
        return self.username       #username来自与AbstractUser
