from django.db import models
from django.db.models.fields import AutoField, CharField, FloatField
from datetime import datetime


class site(models.Model):
    site_name=models.CharField(max_length=200, null=True)
    site_short_name=models.CharField(max_length=200, null=True)
    site_logo=models.ImageField(upload_to='static')
    site_description=models.TextField(max_length=1000, null=True)
    site_description_footer=models.TextField(max_length=1000, null=True)
    site_mail=models.CharField(max_length=200, null=True)
    site_phone=models.CharField(max_length=200, null=True)
    def __str__ (self):
        return self.site_name


class social_media_link(models.Model):
    social_media_name=models.CharField(max_length=200, null=True)
    social_media_link=models.CharField(max_length=200, null=True)
    social_media_username=models.CharField(max_length=200, null=True)
    social_media_logo=models.ImageField(upload_to='static')
    height=models.CharField(max_length=200, null=True)
    width=models.CharField(max_length=200, null=True)
    def __str__ (self):
        return self.social_media_name


class blog_data(models.Model):
    name=models.CharField(max_length=200, null=True)
    message=models.CharField(max_length=500, null=True)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name

class feedback_form(models.Model):
    name=models.CharField(max_length=200, null=True)
    e_mail=models.CharField(max_length=200, null=True)
    feedback=models.CharField(max_length=500, null=True)
    def __str__ (self):
        return self.name


class slider(models.Model):
    image=models.ImageField(upload_to='static')
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(max_length=500, null=True)
    div_style=models.CharField(max_length=500, null=True)
    button_format=models.CharField(max_length=500, null=True)
    button_link=models.CharField(max_length=200, null=True)
    def __str__ (self):
        return self.title


class certification(models.Model):
    image=models.ImageField(upload_to='static')


class code(models.Model):
    name=models.CharField(max_length=200, null=True)
    link=models.CharField(max_length=300, null=True)
    code=models.TextField(max_length=100000, null=True)
    def __str__ (self):
        return self.name


class python_project(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    video_link=models.CharField(max_length=300, null=True)
    about_1=models.TextField(max_length=500, null=True)
    about_2=models.TextField(max_length=500, null=True)
    about_3=models.TextField(max_length=500, null=True)
    def __str__ (self):
        return self.name


class scratch_project(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    video_link=models.CharField(max_length=300, null=True)
    about_1=models.TextField(max_length=500, null=True)
    about_2=models.TextField(max_length=500, null=True)
    about_3=models.TextField(max_length=500, null=True)
    def __str__ (self):
        return self.name


class basic_project(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    video_link=models.CharField(max_length=300, null=True)
    about_1=models.TextField(max_length=500, null=True)
    about_2=models.TextField(max_length=500, null=True)
    about_3=models.TextField(max_length=500, null=True)
    def __str__ (self):
        return self.name


class arduino_project(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    video_link=models.CharField(max_length=300, null=True)
    about_1=models.TextField(max_length=500, null=True)
    about_2=models.TextField(max_length=500, null=True)
    def __str__ (self):
        return self.name


class code_login(models.Model):
    name=models.CharField(max_length=200, null=True)
    e_mail=models.CharField(max_length=300, null=True)
    def __str__ (self):
        return self.name
        
# Create your models here.
