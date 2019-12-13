from django.urls import include, path
from . import views
from django.shortcuts import render
from django.conf.urls import url

urlpatterns = [
	url('',views.detail_danusan,name='detail'),
]