from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class AuthenticationTest(APITestCase):
    fixtures = ['auth', 'users']

    def test_login(self):
        url = '/api/v1/auth/login/'

        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Wrong password
        data = {'username': 'user', 'password': '123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # No account
        data = {'username': 'abc', 'password': 'abc'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_register(self):
        register_url = '/api/v1/accounts/'
        login_url = '/api/v1/auth/login/'

        # Create user and then login
        data = {
            'user': {
                'username': 'abc',
                'password': 'abc',
                'email': 'abc@example.com'
            }
        }
        response = self.client.post(register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {'username': 'abc', 'password': 'abc'}
        response = self.client.post(login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
