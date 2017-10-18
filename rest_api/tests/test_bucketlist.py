from .test_setup import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework import status


class BucketlistTestCase(BaseTestCase):
    """This class contains tests for the bucketlist."""

    def test_bucketlist_create(self):
        self.client.force_authenticate(user=self.test_user)
        self.bucketlist_data = {'name': 'Write a book', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bucketlist_create_unauthorized_access(self):
        self.bucketlist_data = {'name': 'Write a book', 'created_by': self.test_user.id}
        response = self.new_client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_bucketlist_create_duplicates(self):
        self.client.force_authenticate(user=self.test_user)
        self.bucketlist_data = {'name': 'Snack tasting', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_bucketlists(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(
                   '/bucketlists/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_bucketlists_unauthorized_access(self):
        response = self.client.get(
                   '/bucketlists/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
