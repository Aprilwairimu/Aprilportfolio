from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ("comment",)
        
       
	