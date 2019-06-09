#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/12 18:55'

from django import forms
from .models import ArticleConment

class CommentForm(forms.ModelForm):
    class Meta:
        model = ArticleConment
        '''model = Comment 表明这个表单对应的数据库模型是 ArticleComment 类
                   fields指明Form表单要显示的字段
        '''
        fields = ['text','user']