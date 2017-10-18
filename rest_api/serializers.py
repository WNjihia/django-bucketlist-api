from rest_framework import serializers
from .models import Bucketlist
import re


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

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
