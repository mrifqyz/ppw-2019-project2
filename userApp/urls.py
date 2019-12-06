from django.urls import path, include
from .views import managePage

urlpatterns = [
    path('kelola', managePage, name='kelola'),
]