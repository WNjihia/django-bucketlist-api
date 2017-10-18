from django.db import models
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bucketlists', editable=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
