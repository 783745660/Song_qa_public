#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/7 17:10'
import views
from views import LoginView
from django.conf.urls import url

app_name = 'Users'
urlpatterns = [
    url(r'register/',views.register,name='register'),
    url(r'login/',LoginView.as_view(),name='login'),
    url(r'logout/',views.Logout,name='logout'),
    url(r'forget/',views.Forgetpassword,name='forgetpassword'),
    url(r'head/',views.head,name='head'),
    url(r'add/',views.add,name='add'),
    url(r'set/',views.set,name='set'),
    url(r'message/',views.message,name='message'),
    url(r'user_index/',views.user_detail,name='user_index'),
    url(r'user_home/',views.user_home,name='user_home'),
]
