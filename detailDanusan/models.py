from django.db import models
from django_extensions.db.fields import AutoSlugField
from danusan.models import Danusan

class DanusanDetail(models.Model):
	nama = models.CharField(max_length=30000, blank=False)
	price = models.PositiveIntegerField(blank=False)
	gambar = models.CharField(max_length=30000, blank=False)
	slug = AutoSlugField(populate_from='nama')
	detail = models.ForeignKey(Danusan, on_delete=models.CASCADE, default=1,null=True)

	def __str__(self):
		return self.nama

	class Meta:
		ordering = ['nama']

class ReviewModel(models.Model):
	Nama = models.CharField(max_length=300, blank=False)
	Review = models.CharField(max_length=30000, blank=False)
	Time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.review
