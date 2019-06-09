#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/16 17:18'

from django import template
from ..models import Article,Category,Tag
from django.db.models.aggregates import Count

register = template.Library()

'''03获取文章分类
'''
@register.simple_tag
def get_categories():
    #这里的Category.objects.annotate方法也会返回数据库中全部的Category记录，
    # 但是使用Cout()方法返回与每条category记录关联的Article记录的行数
    #使用filter()过滤器过滤掉文章数小于1的分类，即如果该分类下没有文章，那么就不显示该分类
    return Category.objects.all()