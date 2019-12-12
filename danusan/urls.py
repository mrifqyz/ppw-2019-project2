from django.urls import path
from .views import index, add_danusan, get_danusan, login#, delete_danusan

urlpatterns = [
	path('', index, name='index_danusan'),
	path('add_danusan/', add_danusan, name='add_danusan'),
	path('get_danusan/', get_danusan, name='get_danusan'),
	# path('delete_danusan/<int:id>/', delete_danusan, name='delete_danusan'),
	path('login', login, name='login'),
]
