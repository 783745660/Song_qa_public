#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/17 20:15'

from django import forms
from models import Article

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article                                     #指明要创建的form来源于哪一个数据模型
        fields = ['title','tag','content','image']                  #指明Form中要显示的表单字段，而这些字段都来自于Article数据模型


