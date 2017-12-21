# -*- coding: utf-8 -*-
# bulid by Bean_Wei/ 2017/12/20 4:52

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','text']