from django.test import LiveServerTestCase, TestCase, Client
from django.urls import resolve
from .views import *
from .forms import ReviewForm
from .models import ReviewModel

class UnitTest(TestCase):
	def test_apakah_url_bisa_diakses (self):
		response = Client().get('//')
		self.assertEqual(response.status_code, 200)

	def test_url_memanggil_detailDanusanviews(self):
		found = resolve('/')
		self.assertEqual(found.func, main)

	def test_views_memanggil_html_detailDanusan(self):
		response = Client().get('//')
		self.assertTemplateUsed(response, 'main.html')

	def test_apakah_punya_box_form(self):
		response = Client().get('//')
		content = response.content.decode('utf8')
		self.assertIn("<form", content)

	def test_apakah_ada_button_submit(self):
		response = Client().get('//')
		content = response.content.decode('utf8')
		self.assertIn("<button", content) 
		self.assertIn("Post", content) 

	def test_ada_table_isi_review(self):
		response = Client().get('//')
		content = response.content.decode('utf8')
		self.assertIn("<table", content) 
		self.assertIn("Review", content) 
		self.assertIn("Tulis Review", content) 

	def test_apakah_teks_box_kosong_diterima_sebagai_nama(self):
		yang_mau_dites = ReviewForm(data= {'Nama': ''})
		self.assertFalse(yang_mau_dites.is_valid())
		self.assertEqual(yang_mau_dites.errors['Nama'], ["This field is required."])

	def test_apakah_teks_box_kosong_diterima_sebagai_review(self):
		yang_mau_dites_2 = ReviewForm(data= {'Review': ''})
		self.assertFalse(yang_mau_dites_2.is_valid())
		self.assertEqual(yang_mau_dites_2.errors['Review'], ["This field is required."])

	def test_apakah_model_bisa_bikin_review_atau_tidak(self):
		review_baru = ReviewModel.objects.create(Review = 'Bahannya nyaman banget')
		review_status = ReviewModel.objects.all().count()
		self.assertEqual(review_status, 1)