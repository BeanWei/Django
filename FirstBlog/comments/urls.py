# -*- coding: utf-8 -*-
# bulid by Bean_Wei/ 2017/12/20 5:44

from django.conf.urls import url

from .import views

app_name='comments'
urlpatterns=[
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
]