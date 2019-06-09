#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/12 19:37'

from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns =[
    url('article/(?P<article_pk>[0-9]+)/',views.article_comment,name='article_comment'),
]
