# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title=models.CharField(max_length=20)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    #关联数据库
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    views=models.PositiveIntegerField(default=0)
    #User为Django内建模型
    author=models.ForeignKey(User)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    class Meta:
        ordering=['-created_time']


