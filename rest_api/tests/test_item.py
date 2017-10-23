from .test_setup import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework import status


class BucketlistItemTestCase(BaseTestCase):
    """This class contains tests for the bucketlist item."""

    def test_item_create(self):
        """Test for successful creation of an item."""
        self.item_data = {'name': 'Aussie snacks',
                          'bucket': self.test_bucketlist.id}
        response = self.client.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_create_unauthorized_access(self):
        """Test for creation of an item by an unauthorized user."""
        self.item_data = {'name': 'Aussie snacks',
                          'bucket': self.test_bucketlist.id}
        response = self.newclient.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_item_create_duplicates(self):
        """Test for creation of an item that already exists."""
        self.item_data = {'name': 'Aussie snacks',
                          'bucket': self.test_bucketlist.id}
        self.client.post(reverse('create'), self.item_data, format="json")
        response = self.client.post(
                   reverse('create'),
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_item_create_invalid_name_format(self):
        """Test for creation of an item with an invalid name format."""
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
        """Test retrieval of items successfully."""
        response = self.client.get(
                   '/bucketlists/1/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_items_unauthorized_access(self):
        """Test for retrieval of items by an unauthorized user."""
        response = self.newclient.get(
                   '/bucketlists/1/items/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        """Test retrieval of an item by ID."""
        response = self.client.get(
                   '/bucketlists/1/items/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_that_does_not_exist(self):
        """Test for retrieval of an item that does not exist."""
        response = self.client.get(
                   '/bucketlists/1/items/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_item(self):
        """Test updating an item by ID."""
        self.item_data = {'name': 'South African snacks'}
        response = self.client.put(
                   '/bucketlists/1/items/1/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item_invalid_name_format(self):
        """Test updating an item with an invalid name format."""
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
        """Test updating an item that does not exist."""
        self.item_data = {'name': 'Food tasting'}
        response = self.client.put(
                   '/bucketlists/1/items/4/',
                   self.item_data,
                   format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_item(self):
        """Test deleting an item by ID."""
        response = self.client.delete(
                   '/bucketlists/1/items/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_item_that_does_not_exist(self):
        """Test deleting an item that does not exist."""
        response = self.client.delete(
                   '/bucketlists/1/items/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
