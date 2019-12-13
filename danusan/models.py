from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Danusan(models.Model):
	image = models.CharField(max_length=30000, blank=True)
	name = models.CharField(max_length=30, blank=False)	
	price = models.PositiveIntegerField(blank=False)
	datetime = models.DateTimeField(auto_now_add = True)

	User = get_user_model()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = AutoSlugField(populate_from='nama')

	class Meta:
		ordering = ['datetime']


