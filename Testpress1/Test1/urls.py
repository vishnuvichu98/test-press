"""Testpress1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Test1 import views
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^index',index,name='index'),
    url(r'^$',index,name='index'),
    url(r'^quiz',quiz,name='quiz'),
    url(r'^admit_student',admitstudent,name='admitstudent'),
    url(r'^admin_login',adminlogin,name='adminlogin'),
    url(r'^admin_authenticate',adminauthenticate,name='adminauthenticate'),
    url(r'^admin_logout',logout,name='logout'),
    url(r'^admin_dashboard',admindashboard,name='admindashboard'),
    url(r'^add_question',addquestions,name='addquestions')
]
