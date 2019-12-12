from django.urls import path
from .views import index, bantuan, submit

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='home'),
    path('bantuan', bantuan, name='bantuan'),
    path('submit', submit, name='submit'),
]