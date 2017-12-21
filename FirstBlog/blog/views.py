# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from .models import Post,Category,Tag
# Create your views here.

def index(request):
    posts=Post.objects.all().order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',context={'post_list':post_list})
    #return render(request,'base.html')

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form=CommentForm()
    comment_list=post.comment_set.all()
    context={'post':post,
             'form':form,
             'comment_list':comment_list
             }
    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    posts=Post.objects.filter(created_time__year=year,
                                  created_time__month=month
                                  ).order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    posts=Post.objects.filter(category=cate).order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def tags(request,pk):
    tags=get_object_or_404(Tag,pk=pk)
    post_list=Post.objects.filter(tags=tags).order_by('-created_time')
    return render(request,'blog/section.html',context={'post_list':post_list})

def section(request):
    posts=get_object_or_404(Post,pk=pk)
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def artical(request):
    posts=Post.objects.all().order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def source(request):
    cate=get_object_or_404(Category,name='source')
    posts=Post.objects.filter(category=cate).order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def books(request):
    cate=get_object_or_404(Category,name='books')
    posts=Post.objects.filter(category=cate).order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def diary(request):
    cate=get_object_or_404(Category,name='diary')
    posts=Post.objects.filter(category=cate).order_by('-created_time')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'post_list':post_list})

def search(request):
    query=request.GET.get('query')
    error_msg=''
    if not query:
        error_msg='请输入关键词'
        return render(request,'blog/section.html',{'error_msg':error_msg})
    posts=Post.objects.filter(title__icontains=query)
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/section.html',context={'error_msg':error_msg,
                                                       'post_list':post_list})