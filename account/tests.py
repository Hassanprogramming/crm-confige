from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_register_view(self):
        # Test GET request to registration page
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

        # Test POST request with valid data
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(response.url, reverse('home'))

        # Verify that the user is created in the database
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

    def test_login_view(self):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='testpassword')

        # Test GET request to login page
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        # Test POST request with valid login credentials
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(response.url, reverse('home'))

        # Verify that the user is now logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        # Create a test user and log them in
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Test GET request to logout view
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(response.url, reverse('login'))

        # Verify that the user is now logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)
