#coding=utf-8

from __future__ import unicode_literals
import datetime
from django.db import models
from Users.models import UserProfile
from blog.models import Article
from django.utils import timezone
import django.utils.datetime_safe

# Create your models here.

'''创建评论用户模型
'''
class BaseConment(models.Model):
    '''基础评论模型'''
    text = models.TextField(verbose_name=u'评论内容')
    conment_time = models.DateTimeField(auto_now_add=True,editable=True,verbose_name='评论时间')
    user = models.CharField(max_length=20,verbose_name=u'评论者')


    class Meta:
        verbose_name_plural = verbose_name = u'基础评论'
        abstract = True    #此声明的作用是声明该类是一个抽象模型，不需要数据迁移。但是该元数据不会被子类继承
    #
    # def __unicode__(self):
    #     return self.text[:20]


class ArticleConment(BaseConment):
    '''一级文章评论模型，即对文章进行评论'''
    comment_aticle = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_comments',verbose_name=u'评论文章')
    poll_nums = models.IntegerField(default=0, verbose_name=u'点赞')

    class Meta:
        verbose_name_plural = verbose_name = u'文章评论'
        ordering = ['-conment_time']

    def __unicode__(self):
        return self.text[:20]

class ArticleConmentReply(BaseConment):
    '''二级文章评论模型，即对回复一级评论，并可相互评论'''
    comment = models.ForeignKey(ArticleConment,on_delete=models.CASCADE,related_name='excomment',verbose_name=u'评论一级评论')
    reply = models.ForeignKey('self',blank=True,default=u'',on_delete=models.CASCADE,verbose_name=u'用户间评论')
    poll_nums = models.IntegerField(default=0, verbose_name=u'点赞')

    class Meta:
        verbose_name_plural = verbose_name = u'用户互评'
        ordering = ['conment_time']

    def __unicode__(self):
        return self.reply



