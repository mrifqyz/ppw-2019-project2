from django.db import models

# Create your models here.
class Bantuan(models.Model):
    pertanyaan = models.CharField(max_length=100)
    jawaban = models.TextField(blank=True)
    nama = models.CharField(max_length=50)
    waktu = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pertanyaan;
