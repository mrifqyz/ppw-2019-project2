from django.test import TestCase, Client
from django.urls import resolve
from .views import index

# Create your tests here.
class UnitTest(TestCase):
    def test_buka_homepage(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_homepage_pake_fungsi_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_ada_navbar(self):
        response = Client().get('')
        self.assertContains(response, '<nav')
    
    def test_ada_footer(self):
        response = Client().get('')
        self.assertContains(response, '</footer>')

    def test_ada_nama_DNA(self):
        response = Client().get('')
        self.assertContains(response, 'DNA')
    
    def test_ada_gambar(self):
        response = Client().get('')
        self.assertContains(response, 'image.png')

    def test_ada_button_sign_up(self):
        response = Client().get('')
        self.assertContains(response, '</button>')

    def test_ada_ajakan_ngedanus(self):
        response = Client().get('')
        self.assertContains(response, 'Yuk bergabung dengan kami')

    def test_ada_deskripsi_DNA(self):
        response = Client().get('')
        self.assertContains(response, 'Sebuah platform buat kamu')