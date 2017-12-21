# -*- coding: utf-8 -*-
# bulid by Bean_Wei/ 2017/12/18 23:49

from ..models import Post,Category,Tag
from django.db.models.aggregates import Count
from django import template

register=template.Library()

@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag()
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))#.filter(num_posts_gt=0)

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.simple_tag()
def get_articals():
    return Post.objects.all().order_by('-created_time')

@register.simple_tag()
def get_sources():
    return Post.objects.filter(name='source').order_by('-created_time')

@register.simple_tag()
def get_books():
    return Post.objects.filter(category='books').order_by('-created_time')

@register.simple_tag()
def get_diarys():
    return Post.objects.filter(category='diary').order_by('-created_time')