#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from Users.models import UserProfile
from django.core.urlresolvers import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'标签')
    class Meta:
        verbose_name_plural = verbose_name = u'标签'
    def __unicode__(self):
        return self.name


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,unique=True,verbose_name=u'类别')
    desc = models.TextField(verbose_name=u'详情')
    class Meta:
        verbose_name_plural = verbose_name = u'类别'
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'姓名')
    profile = models.CharField(max_length=20,default='',verbose_name=u'账号')
    password = models.CharField(max_length=20,verbose_name=u'密码')
    register_date = models.DateTimeField(auto_now_add=True,editable=True)
    class Meta:
        verbose_name_plural = verbose_name = u'作者信息'
    def __unicode__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('Users.UserProfile',on_delete=models.DO_NOTHING,default=1,verbose_name=u'作者')
    title = models.CharField(max_length=50,verbose_name=u'标题')
    abstract = models.CharField(max_length=300,verbose_name=u'摘要',blank=True,null=True)
    content = models.TextField(verbose_name=u'内容')
    pub_date = models.DateTimeField(auto_now_add=True,editable=True)
    tag = models.ForeignKey(Tag,on_delete=models.SET_DEFAULT,default=1,verbose_name=u'标签')
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=1,verbose_name=u'类别')
    image = models.ImageField(max_length=100,upload_to='article/%y/%m',default='article/19/05/nv3.jpg',verbose_name=u'封面')
    views_num = models.PositiveIntegerField(default=0,blank=True,null=True) #非负性
    poll_num = models.IntegerField(default=0,verbose_name=u'点赞',blank=True,null=True)
    keep_num = models.IntegerField(default=0,verbose_name=u'收藏',blank=True,null=True)

    class Meta:
        verbose_name_plural = verbose_name = u'文章管理'
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def increase_views_num(self):
        self.views_num += 1
        self.save(update_fields=['views_num'])

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

