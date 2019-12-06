from django.contrib import admin
from django.urls import path, include
from userApp.views import loginPage, registerPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('kelola', include('userApp.urls')),
]
