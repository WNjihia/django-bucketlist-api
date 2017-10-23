from .test_setup import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework import status


class BucketlistItemTestCase(BaseTestCase):
    """This class contains tests for the bucketlist item."""

    def test_item_create(self):
        self.item_data = {'name': 'Aussie snacks',
                          'bucket': self.test_bucketlist.id}
        response = self.client.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_create_unauthorized_access(self):
        self.item_data = {'name': 'Aussie snacks',
                          'bucket': self.test_bucketlist.id}
        response = self.newclient.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_item_create_invalid_name_format(self):
        self.item_data = {'name': '', 'bucket': self.test_bucketlist.id}
        response = self.client.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.item_data = {'name': '@#$%^&*', 'bucket': self.test_bucketlist.id}
        response = self.client.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_items(self):
        response = self.client.get(
                   '/bucketlists/1/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_items_unauthorized_access(self):
        response = self.newclient.get(
                   '/bucketlists/1/items/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        response = self.client.get(
                   '/bucketlists/1/items/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_that_does_not_exist(self):
        response = self.client.get(
                   '/bucketlists/1/items/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_item(self):
        self.item_data = {'name': 'South African snacks'}
        response = self.client.put(
                   '/bucketlists/1/items/1/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bucketlist_invalid_name_format(self):
        self.item_data = {'name': ''}
        response = self.client.put(
                   '/bucketlists/1/items/1/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.item_data = {'name': '@#$%^&*'}
        response = self.client.put(
                   '/bucketlists/1/items/1/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_item_that_does_not_exist(self):
        self.item_data = {'name': 'Food tasting'}
        response = self.client.put(
                   '/bucketlists/1/items/4/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_item(self):
        response = self.client.delete(
                   '/bucketlists/1/items/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_item_that_does_not_exist(self):
        response = self.client.delete(
                   '/bucketlists/1/items/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
