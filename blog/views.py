#coding=utf-8
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger,Paginator
from models import Article,Category,UserProfile
from comment.forms import CommentForm
from forms import AddArticleForm

from django.db.models import Q
# Create your views here.

# class IndexView(View):
#     return cdf

#主页显示所有文章
def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()

    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(article_list,5,request=request)

    latest_article_list = p.page(page)

    context = {'latest_article_list':latest_article_list,
               'category_list':category_list,
               }
    # print latest_article_list
    return render(request,'blog/index.html',context)
    # return redirect(request,'/blog/index/')

#
# def detail(request,pk):
#     article = get_object_or_404(Article,pk=pk)
#     context = {'article':article,
#                }
#     return render(request,'blog/detail.html',context=context)


#点击每篇文章标题后查看文章详情
def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.increase_views_num()
    comment_list = article.article_comments.all()
    form = CommentForm()
    context = {'article':article,
               'comment_list':comment_list,
               'form':form
               }
    return  render(request,'blog/detail.html',context=context)


#获取各分类下的文章
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    article_list = cate.article_set.all()
    category_list = Category.objects.all()
    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(article_list,5,request=request)

    latest_article_list = p.page(page)
    context = {'latest_article_list': latest_article_list,
               'category_list':category_list,
               }
    # return HttpResponseRedirect('/blog/index/')
    print latest_article_list
    return render(request,'blog/index.html',context=context)


def AddArticle(request):

    if request.method == 'POST':

        article_tag = request.POST.get('tag','')
        article_title = request.POST.get('title','')
        article_content = request.POST.get('content','')
        add_article_form = AddArticleForm(request.POST)

        print article_tag
        print article_title
        print article_content
        print add_article_form.errors
        if add_article_form.is_valid():
           article = add_article_form.save(commit=False)
           article.author = request.user
           article.save()
           return  redirect('/blog/index')

        else:
            return  HttpResponseRedirect('/')

    else:
        return redirect('/user/add/')









