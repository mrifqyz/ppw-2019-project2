from django.contrib import admin
from django.urls import path, include
from userApp.views import loginPage, registerPage, signOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('kelola', include('userApp.urls')),
    path('danusan/', include('danusan.urls')),
    path('', include('app1.urls')),
    path('dfj90d21lf@34a12', signOut, name='logout')
]
