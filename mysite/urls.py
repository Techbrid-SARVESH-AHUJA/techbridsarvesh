"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

admin.site.site_header = "Techbrid Sarvesh Dashboard"
admin.site.site_title = "Techbrid Sarvesh"
admin.site.index_title = "ADMIN"

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    
    path('my_projects/', views.my_projects, name="my_projects"),
    
    path('python_projects_codes/', views.python_projects_codes, name="python_projects_codes"),
    
    path('feedback/', views.feedback, name="feedback"),

    path('blog/', views.blog, name="blog"),

    path('certifications/', views.certifications, name="certifications"),

    path('python_projects/<str:pk_prod>/', views.python_projects, name="python_projects"),

    path('arduino_projects/<str:pk_prod>/', views.arduino_projects, name="arduino_projects"),

    path('scratch_projects/<str:pk_prod>/', views.scratch_projects, name="scratch_projects"),

    path('basic_electronics_projects/<str:pk_prod>/', views.basic_electronics_projects, name="basic_electronics_projects"),

    path('view_codes/<str:pk_prod>/', views.view_codes, name="view_codes"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
