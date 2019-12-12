from django.test import TestCase, Client
from .models import User
# Create your tests here.


class UserAppTest(TestCase):
    def setUp(self):
        self.userData = {
            'username': 'mohamad.rifqy@ui.ac.id',
            'password': 'ssrifdiza',
            'fullname': 'Mohamad Rifqy Zulkarnaen',
            'password1': 'ssrifdiza',
            'password2': 'ssrifdiza',
            'phone': '087777535288',
            'bio': 'Tes satu satu hahaha'
        }

        self.adminData = {
            'username': 'testcase@ui.ac.id',
            'password': 'eyanksubur'
        }

        self.stafData = {
            'username': 'staffuser@ui.ac.id',
            'password': 'wadidawwadaw'
        }
        self.user = User.objects.create_user('mohamad.rifqy@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
                                             'Tes satu satu hahaha', '087777535288', 'ssrifdiza')

        self.superuser = User.objects.create_superuser('testcase@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
                                                       'Tes satu satu hahaha', '087777535288', 'eyanksubur')

        self.staffuser = User.objects.create_staffuser('staffuser@ui.ac.id', 'Mohamad Rifqy Zulkarnaen',
                                                       'Tes satu satu hahaha', '087777535288', 'wadidawwadaw')

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
        self.assertEqual(User.objects.all().count(), 3)

    def test_user_login(self):
        response = self.client.post('/login', data=self.userData, follow=True)
        # print(response.context['user'].is_active)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_register_users(self):
        toBeRegistered = {
            "username": "zheyenk@gmail.com",
            "fullname": "cinoy",
            "bio": "haha",
            "phone": "081315681216",
            "password1": "cinoyganteng",
            "password2": "cinoyganteng",
        }

        response = self.client.post(
            '/register', data=toBeRegistered, follow=True)
        self.assertEqual(User.objects.all().count(), 4)

    def test_user_logout(self):
        response = self.client.post('/login', data=self.userData, follow=True)
        response = self.client.get('/dfj90d21lf@34a12', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_staff_user(self):
        response = self.client.post('/login', data=self.stafData, follow=True)
        self.assertTrue(response.context['user'].is_staff)

    def test_admin_user(self):
        response = self.client.post('/login', data=self.adminData, follow=True)
        self.assertTrue(response.context['user'].is_admin)

    def test_user_register_has_no_email(self):
        toBeRegistered = {
            "email": "",
            "full_name": "cinoy",
            "bio": "haha",
            "phone_number": "081315681216",
            "password": "cinoyganteng",
        }
        with self.assertRaises(ValueError) as error:
            User.objects.create_user(**toBeRegistered)

    def test_user_register_has_no_password(self):
        toBeRegistered = {
            "email": "cinoy@ganteng.com",
            "full_name": "cinoy",
            "bio": "haha",
            "phone_number": "081315681216",
            "password": "",
        }
        with self.assertRaises(ValueError) as error:
            User.objects.create_user(**toBeRegistered)