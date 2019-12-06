from django.test import TestCase, Client
from .models import User

# Create your tests here.
class UserAppTest(TestCase):
    def test_url_login(self):
        c = Client()
        response = c.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_url_logout(self):
        c = Client()
        response = c.get("/logout")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "logout.html")

    def test_url_user_profile(self):
        c = Client()
        response = c.get("/kelola")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kelola.html")

    def test_create_user(self):
        User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
        'Tes satu satu hahaha', '087777535288', 'ssrifdiza')
        self.assertEqual(User.objects.all().count(), 1)

    

