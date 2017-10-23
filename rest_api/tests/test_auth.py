from .test_setup import BaseTestCase
from django.contrib.auth.models import User


class UserAuthAPIView(BaseTestCase):
    """This class contains tests for user registration and log in."""

    def test_register_new_user(self):
        """Tests a new user can be succesfully registered."""
        self.user_data = {'username': 'janedoe',
                          'password': 'password'}
        response = self.client.post('/register/', self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.last().username, 'janedoe')

    def test_register_existing_user(self):
        """Tests a new user can be succesfully registered."""
        self.user_data = {'username': 'testuser',
                          'password': 'password'}
        response = self.client.post('/register/', self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_user_registration_with_invalid_username(self):
        """Test for user registration with inavlid username."""
        self.user_data = {'username': '',
                          'password': 'password'}
        response = self.client.post('/register/', self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_user_can_login(self):
        """Test for successful user login."""
        self.user_data = {'username': 'janedoe',
                          'password': 'password'}
        self.client.post('/register/', self.user_data)
        response = self.client.post('/login/', self.user_data)
        self.assertContains(response, 'token')

    def test_user_login_with_invalid_credentials(self):
        """Test for successful user login."""
        self.user_data = {'username': 'johndoe',
                          'password': 'password'}
        response = self.client.post('/login/', self.user_data)
        self.assertEqual(response.status_code, 400)
