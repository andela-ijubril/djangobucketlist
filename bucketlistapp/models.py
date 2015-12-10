from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bucketlist(BaseModel):

    name = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, related_name="bucketlist")


class BucketlistItem(BaseModel):

    name = models.CharField(max_length=500, blank=True)
    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(Bucketlist, related_name="items")
