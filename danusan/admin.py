from django.contrib import admin
from .models import Danusan

# Register your models here.
class DanusanAdmin(admin.ModelAdmin):
	class Meta:
		model = Danusan


admin.site.register(Danusan, DanusanAdmin)
