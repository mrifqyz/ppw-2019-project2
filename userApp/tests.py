from django.test import TestCase, Client
from .models import User
from django.contrib.auth import login, logout

# Create your tests here.
class UserAppTest(TestCase):
    def setUp(self):
        self.userData = {
            'username':'mohamad.rifqy@ui.ac.id',
            'password':'ssrifdiza'
        }
        User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
        'Tes satu satu hahaha', '087777535288', 'ssrifdiza')

    def test_url_login(self):
        c = Client()
        response = c.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_url_logout(self):
        c = Client()
        response = c.get("/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_url_user_profile(self):
        c = Client()
        response = c.get("/kelola")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kelola.html")

    def test_create_user(self):
        self.assertEqual(User.objects.all().count(), 1)