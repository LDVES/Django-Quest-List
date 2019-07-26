from django.test import TestCase
from django.test import Client

class TestRenderingAuthForms(TestCase):
    client = Client()

    def test_rendering_forms(self):
        response_login = self.client.get('/login')
        response_register = self.client.get('/register')
        self.assertEqual(response_login.status_code, 200)
        self.assertEqual(response_register.status_code, 200)

    def test_sending_data_to_login_form(self):
        response = self.client.post('/login', { 'username' : 'test_user', 'password' : 'password' })
        self.assertEqual(response.status_code, 302)

    def test_sending_data_to_login_form(self):
        response = self.client.post('/register', { 'username' : 'test_user', 'password' : 'password', 'password1' : 'password' })
        self.assertEqual(response.status_code, 200)
