from rest_framework.test import APITestCase
from rest_api.models import Bucketlist
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class BaseTestCase(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.test_user = User.objects.create(username="testuser",
                                             password="password")
        self.test_bucketlist = Bucketlist.objects.create(name="Snack tasting",
                                                         created_by=self.test_user)

        self.client = APIClient()
        self.client.force_authenticate(user=self.test_user)
        self.newclient = APIClient()
