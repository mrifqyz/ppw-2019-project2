from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Danusan(models.Model):
	image = models.CharField(max_length=30000, blank=True)
	name = models.CharField(max_length=30, blank=False)	
	price = models.PositiveIntegerField(blank=False)
	datetime = models.DateTimeField(auto_now_add = True)

	user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)

	class Meta:
		ordering = ['-datetime']
