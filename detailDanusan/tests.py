from django.test import LiveServerTestCase, TestCase, Client
from django.urls import resolve
from .views import *
from danusan.models import Danusan
from userApp.models import User
from .forms import ReviewForm
from .models import ReviewModel

class UnitTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user('testcase@test.com', 'testguy',
                                             'Tes satu satu hahaha', '0981131343', 'nasigoreng')
		self.danusan = Danusan.objects.create(name="Martabak Telor",
			price="2000", 
			image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/MartabakTelur.JPG/1200px-MartabakTelur.JPG",
			user=self.user)

	def test_apakah_url_bisa_diakses (self):
		response = Client().get('/danusan/'+self.danusan.slug)
		self.assertEqual(response.status_code, 200)

	def test_apakah_konten_terpakai(self):
		response = Client().get('/danusan/'+self.danusan.slug)
		content = response.content.decode('utf8')
		self.assertIn("<form", content)
		self.assertTemplateUsed(response, "detail.html")
		self.assertIn("<button", content) 
		self.assertIn("Post", content) 
		self.assertIn("<table", content) 
		self.assertIn("Review", content) 
		self.assertIn("Tulis Review", content) 

	def test_apakah_teks_box_kosong_diterima_sebagai_nama(self):
		yang_mau_dites = ReviewForm(data= {'nama': ''})
		self.assertFalse(yang_mau_dites.is_valid())
		self.assertEqual(yang_mau_dites.errors['nama'], ["This field is required."])

	def test_apakah_teks_box_kosong_diterima_sebagai_review(self):
		yang_mau_dites_2 = ReviewForm(data= {'review': ''})
		self.assertFalse(yang_mau_dites_2.is_valid())
		self.assertEqual(yang_mau_dites_2.errors['review'], ["This field is required."])

	def test_apakah_model_bisa_bikin_review_atau_tidak(self):
		review_baru = ReviewModel.objects.create(Review = 'Bahannya nyaman banget')
		review_status = ReviewModel.objects.all().count()
		self.assertEqual(review_status, 1)

	def test_apakah_models_masuk_ke_page(self):
		data={
		'nama':'Icha',
		'review':'Enak kak'
		}
		response = self.client.post('/danusan/'+self.danusan.slug, data=data, follow=True)
		self.assertIn('Icha', response.content.decode())

	def test_url_kalo_gaada_danusannya(self):
		response = Client().get('/danusan/kucing')
		self.assertTemplateUsed("index.html")