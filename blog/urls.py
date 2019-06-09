#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/7 10:36'
from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    url(r'index/',views.index,name='index'),
    url(r'article/(?P<pk>[0-9]+)/',views.detail,name='detail'),
    url(r'add_article/',views.AddArticle,name='add_article'),
    url(r'tag/(?P<pk>[0-9]+)/', views.detail, name='tag'),
    url(r'cate/(?P<pk>[0-9]+)/',views.category,name='category'),
]

