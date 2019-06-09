#coding=utf-8
from django.shortcuts import render,redirect,HttpResponseRedirect,render_to_response,RequestContext
from django.views.generic.base import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import logout
from forms import RegisterForm,LoginForm
from models import UserProfile
from  blog.models import Category,Tag
import blog

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username),Q(password=password))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('email','')
        password_1 = request.POST.get('password','')
        password_2 = request.POST.get('repass','')
        register_form = RegisterForm(request.POST)
        print user_name,password_1
        print register_form.errors

        if register_form.is_valid():
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            # 这一步一定要使用make_password将密码生成哈希值，否则数据库中插入的数据是明文，这将导致用户登录时authenticate()认证失败
            user_profile.password = make_password(password_1)
            user_profile.save()

            return render(request,'user/login.html')
            # return HttpResponseRedirect('/user/login/')

        else:
            return  render(request,'user/reg.html',{'register_form':register_form})

    else:
        return render(request,'user/reg.html')


class LoginView(View):

    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        login_form = LoginForm(request.POST)
        print login_form.errors

        if login_form.is_valid():
            user_name = request.POST.get('email','')
            pass_word = request.POST.get('password','')
            user = authenticate(username=user_name,password=pass_word)
            print user_name,pass_word,user

            if user is not None:
                if user.is_active:

                    login(request,user)
                    # return render(request,'blog/index.html')  #我在使用该方法时发现虽然页面发生变化，但是url没有发生改变
                    return redirect('/blog/index', context_instance = RequestContext(request))
                    # return render_to_response('blog/index.html',{'user':user},RequestContext(request))
                else:
                    return render(request, 'user/login.html', {'msg': '用户尚未激活'})

            else:
                return render(request,'user/login.html',{'msg':'用户名或密码错误!'})

        else:
            return  render(request,'user/login.html',{'login_form':login_form})


def Forgetpassword(request):
    return render(request,'user/forget.html')


def head(request):
    return render(request,'common/header.html')


def add(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    context = {'category_list':category_list,
               'tag_list':tag_list,
               }
    return  render(request,'blog/add.html',context=context)


def set(request):
    return render(request,'user/set.html')


def message(request):
    return render(request,'user/message.html')


def user_detail(request):
    return render(request,'user/index.html')


def user_home(request):
    return render(request,'user/home.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/index/')   #调用logout()函数后，目前已登录的用户session数据会被清除
