from django.urls import path, re_path
from .views import index, add_danusan, login, danusanJSON#, delete_danusan

urlpatterns = [
	path('', index, name='index_danusan'),
	path('add_danusan', add_danusan, name='add_danusan'),
	# path('delete_danusan/<int:id>/', delete_danusan, name='delete_danusan'),
	path('login', login, name='login'),
	re_path(r'^dnajson&filter=(?P<kw>[\w-]+)&keyword=(?P<val>[\w-]+)', danusanJSON, name="danusJSON"),
	path("jsondata", danusanJSON)
]
