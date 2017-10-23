from .test_setup import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework import status


class BucketlistTestCase(BaseTestCase):
    """This class contains tests for the bucketlist."""

    def test_bucketlist_create(self):
        self.bucketlist_data = {'name': 'Write a book', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bucketlist_create_unauthorized_access(self):
        self.bucketlist_data = {'name': 'Write a book', 'created_by': self.test_user.id}
        response = self.newclient.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bucketlist_create_duplicates(self):
        self.bucketlist_data = {'name': 'Snack tasting', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bucketlist_create_invalid_name_format(self):
        self.bucketlist_data = {'name': '', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.bucketlist_data = {'name': '@#$%^&*', 'created_by': self.test_user.id}
        response = self.client.post(
                   reverse('create'),
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_bucketlists(self):
        response = self.client.get(
                   '/bucketlists/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_bucketlists_unauthorized_access(self):
        response = self.newclient.get(
                   '/bucketlists/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_bucketlist(self):
        response = self.client.get(
                   '/bucketlists/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bucketlist_that_does_not_exist(self):
        response = self.client.get(
                   '/bucketlists/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bucketlist(self):
        self.bucketlist_data = {'name': 'Food tasting'}
        response = self.client.put(
                   '/bucketlists/1/',
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bucketlist_invalid_name_format(self):
        self.bucketlist_data = {'name': ''}
        response = self.client.put(
                   '/bucketlists/1/',
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.bucketlist_data = {'name': '@#$%^&*'}
        response = self.client.put(
                   '/bucketlists/1/',
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_bucketlist_that_does_not_exist(self):
        self.bucketlist_data = {'name': 'Food tasting'}
        response = self.client.put(
                   '/bucketlists/2/',
                   self.bucketlist_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_bucketlist(self):
        response = self.client.delete(
                   '/bucketlists/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_bucketlist_that_does_not_exist(self):
        response = self.client.delete(
                   '/bucketlists/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
