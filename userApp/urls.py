from django.urls import path, include
from .views import managePage

urlpatterns = [
    path('', managePage, name='kelola'),
]