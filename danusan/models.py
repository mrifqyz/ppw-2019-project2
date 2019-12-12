from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Danusan(models.Model):
	image = models.CharField(max_length=30000, blank=True)
	name = models.CharField(max_length=30, blank=False)	
	price = models.PositiveIntegerField(blank=False)
	datetime = models.DateTimeField(auto_now_add = True)

	User = get_user_model()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ['datetime']
