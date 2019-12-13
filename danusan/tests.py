from django.test import TestCase, Client
from .models import Danusan, DanusanDetail, ReviewModel

from userApp.models import User

# Create your tests here.
class UnitTest(TestCase):

	def test_apakah_ada_url_slash(self):
		response = self.client.get('/danusan/')
		self.assertEqual(response.status_code, 200)

	def test_apakah_ada_danusan(self):
		response = self.client.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn('Danusan', content)

	def test_apakah_ada_table(self):
		response = self.client.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn("<table", content)

	def test_get_danusan(self):
		#################
		response = self.client.get('/danusan/get_danusan/')
		self.assertEqual(response.status_code, 200)

	def test_add_danusan(self):
		#################
		response = self.client.post('/danusan/add_danusan/',
			{'image': "link", 'name': "Bakso", 'price': "15000"})
		self.assertEqual(response.status_code, 302)

	def test_apakah_ada_input_submit(self):
		response = self.client.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn("<input", content)
		self.assertIn("submit", content)

	def setUp(self):
		self.user = User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
		'Tes satu satu hahaha', '087777535288', 'ssrifdiza')
		self.client.login(email='mohamad.rifqy@ui.ac.id', password='ssrifdiza')

	def test_apakah_ada_model_danusan_dengan_field_image_name_price_dan_user(self):
	# def test_apakah_ada_model_danusan_dengan_field_image_name_dan_price(self):
		Danusan(image="link", name="Bakso", price="15000", user=self.user).save()
		# Danusan(image="link", name="Bakso", price="15000").save()
		all_danusan = Danusan.objects.all()
		self.assertEqual(all_danusan.count(), 1)
		self.assertEqual(Danusan.objects.get(id=1).name, "Bakso")

class DetailTest(TestCase);
	def test_views_memanggil_html_detailDanusan(self):
		response = Client().get('//')
		self.assertTemplateUsed(response, 'detail.html')

	def test_get_detail(self):
		response = self.client.get('/danusan/get_detail/')
		self.assertEqual(response.status_code, 200)

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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		options.add_argument('--disable-dev-shm-usage')
		self.browser = webdriver.Chrome('./chromedriver', chrome_options=options)
		self.browser.get(self.live_server_url + "/danusan/")

		user = User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
		'Tes satu satu hahaha', '087777535288', 'ssrifdiza')

	def test_secure_page(self):
		self.client.login(email='mohamad.rifqy@ui.ac.id', password='ssrifdiza')

	def tearDown(self):
		self.browser.quit()

	def test_judul(self):
		browser = self.browser
		self.assertIn("Danusan", browser.title)
