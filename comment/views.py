#coding=utf-8
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Article
from .models import ArticleConment
from .forms import CommentForm

# Create your views here.

'''文章评论视图函数类似于用户注册，从从from表单中抽取数据并做验证，
    如果合法将其保存至数据库，并重定向至文章详情页，而文章详情页会将向模板传递文章评论列表字典，
    实现用户评论
'''
def article_comment(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)                    #根据POST请求实例化一个form表单
        if form.is_valid():
            comment = form.save(commit=False)                #根据实例化后的form创建comment对象
            comment.comment_aticle = article                 #将得到的文章和评论关联起来
            comment.save()                                    #将评论保存至数据库
            print comment,request.user
            return  redirect(article)                        #评论成功后重定向到被评论的文章详情页，

        else:
            comment_list = article.article_comments.all()
            context = {'article':article,
                       'form':form,
                       'comment_list':comment_list,
                       }
            print form.errors
            return render(request,'blog/detail.html',context=context)

    else:
        return redirect(article)

