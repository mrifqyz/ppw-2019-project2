from django.test import TestCase, Client
from django.urls import resolve
from .views import index

# Create your tests here.
class UnitTest(TestCase):
    def test_buka_homepage(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_buka_homepage_2(self):
        response = Client().get('/home')
        self.assertEqual(response.status_code, 200)

    def test_homepage_pake_fungsi_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_buka_halaman_bantuan(self):
        response = Client().get('/bantuan')
        self.assertEqual(response.status_code, 200)

    def test_buka_halaman_bantuan_pakai_fungsi_bantuan(self):
        found = resolve('/bantuan')
        self.assertEqual(found.func, bantuan)

    def test_ada_navbar_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, '<nav')
    
    def test_ada_footer_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, '</footer>')

    def test_ada_nama_DNA_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, 'DNA')
    
    def test_ada_gambar_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, 'image.png')

    def test_ada_button_sign_up_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, '</button>')

    def test_ada_ajakan_ngedanus_di_homepage(self):
        response = Client().get('')
        self.assertContains(response, 'Yuk bergabung dengan kami')

    def test_ada_deskripsi_DNA(self):
        response = Client().get('')
        self.assertContains(response, 'Sebuah platform buat kamu')

    def test_bisa_buat_model_bantuan(self):
        response_post = Client().post('/submit', {'pertanyaan' : 'Apa?',
                                                  'jawaban' : 'Iya',
                                                  'nama' : 'Ahmad'})
        self.assertEqual(response_post.status_code, 302)
