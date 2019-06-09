#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/6 19:07'
import xadmin
from .models import ArticleConment,ArticleConmentReply


class ArticleConmentAdmin(object):
    list_display = ('conment_time','user','comment_aticle')

class ArticleConmentReplayAdmin(object):
    list_display =  ('conment_time','user','comment','reply')

xadmin.site.register(ArticleConment,ArticleConmentAdmin)
xadmin.site.register(ArticleConmentReply,ArticleConmentReplayAdmin)


