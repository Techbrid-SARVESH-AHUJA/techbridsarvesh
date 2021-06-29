from django.db.models import fields
from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http.response import FileResponse
from .models import *


class add_blog_data(ModelForm):
    class Meta:
        model=blog_data
        fields=["name", "message"]


class feedback_form(ModelForm):
    class Meta:
        model=feedback_form
        fields='__all__'


class code_login(ModelForm):
    class Meta:
        model=code_login
        fields='__all__'