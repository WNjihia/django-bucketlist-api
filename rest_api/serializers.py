from rest_framework import serializers
from .models import Bucketlist, Item
import re


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Bucketlist instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified', 'created_by')
        read_only_fields = ('date_created', 'date_modified', 'created_by')

    def validate_name(self, value):
        """Checks for duplicates."""
        _name_format = re.compile(r'^[ a-zA-Z0-9_.-]+$')
        if not value or not _name_format.match(value):
            raise serializers.ValidationError("Invalid name")
        return value


class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Item instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Item
        fields = ('id', 'name', 'date_created', 'date_modified', 'bucket')
        read_only_fields = ('date_created', 'date_modified')

    def validate_name(self, value):
        """Checks for duplicates."""
        _name_format = re.compile(r'^[ a-zA-Z0-9_.-]+$')
        if not value or not _name_format.match(value):
            raise serializers.ValidationError("Invalid name")
        return value
