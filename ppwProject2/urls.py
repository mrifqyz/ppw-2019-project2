from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from userApp.views import loginPage, registerPage, signOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('kelola', include('userApp.urls')),
    path('danusan/', include('danusan.urls')),
    path('detaildanusan/', include('detailDanusan.urls')),
    path('', include('app1.urls')),
    path('dfj90d21lf@34a12', signOut, name='logout')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)