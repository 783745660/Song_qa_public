#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/6 11:26'


from .models import Article,Category,Tag,Author
import xadmin


'''注册数据模型
'''

class ArticleAdmin(object):
    list_dispaly = ('author','title','content','abstract','pub_date','image','views_num','tag')


class CategoryAdmin(object):
    list_display = ('name','desc')

class TagAdmin(object):
    list_display = ('name','id')

class AuthorAdmin(object):
    list_display = ('name','profile','password','register_date')

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Author,AuthorAdmin)



