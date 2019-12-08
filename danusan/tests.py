from django.test import TestCase, Client
from .models import Danusan

from userApp.models import User

# Create your tests here.
class UnitTest(TestCase):

	def test_apakah_ada_url_slash(self):
		c = Client()
		response = c.get('/danusan/')
		self.assertEqual(response.status_code, 200)

	def test_apakah_ada_danusan(self):		
		c = Client()
		response = c.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn('Danusan', content)

	def test_apakah_ada_table(self):
		c = Client()
		response = c.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn("<table", content)

	def test_apakah_ada_input_submit(self):
		c = Client()
		response = c.get('/danusan/')
		content = response.content.decode('utf8')
		self.assertIn("<input", content)
		self.assertIn("submit", content)

	def setUp(self):
		self.user = User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
        'Tes satu satu hahaha', '087777535288', 'ssrifdiza')

	# def test_apakah_ada_model_danusan_dengan_field_image_name_price_dan_user(self):
	def test_apakah_ada_model_danusan_dengan_field_image_name_dan_price(self):
		# Danusan(image="link", name="Bakso", price="15000", user=self.user).save()
		Danusan(image="link", name="Bakso", price="15000").save()
		all_danusan = Danusan.objects.all()
		self.assertEqual(all_danusan.count(), 1)
		self.assertEqual(Danusan.objects.get(id=1).name, "Bakso")


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

	# def test_secure_page(self):
	# 	self.client.login(username='temporary', password='temporary')
	# 	response = self.client.get('/manufacturers/', follow=True)
	# 	user = User.objects.get(username='temporary')
	# 	self.assertEqual(response.context['email'], 'temporary@gmail.com')

	def tearDown(self):
		self.browser.quit()

	def test_judul(self):
		browser = self.browser
		self.assertIn("Danusan", browser.title)
