#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/16 16:08'

from haystack import indexes
from .models import Article

''' haystack使用约定：要全文搜索app下数据，需要在该app下创建一个search_indexes.py,
    并且在该文件中创建一个XXindex类，XX 为含有被检索数据的模型
    并且继承 SearchIndex 和 Indexable
    
'''
class ArticleIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) #使用该字段的内容作为索引，text为haystack约定

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()




