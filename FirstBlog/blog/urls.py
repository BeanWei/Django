# -*- coding: utf-8 -*-
# bulid by Bean_Wei/ 2017/12/18 3:19

from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.section,name='section'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
    url(r'^tags/(?P<pk>[0-9]+)/$',views.tags,name='tags'),
    url(r'^artical/$',views.artical,name='artical'),
    url(r'^source/$',views.source,name='source'),
    url(r'^books/$',views.books,name='books'),
    url(r'^diary/$',views.diary,name='diary'),
    url(r'^search/$',views.search,name='search'),
]