from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


class Bucketlist(BaseModel):

    name = models.CharField(max_length=100, blank=True)
    public = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, related_name="buckets")


class BucketlistItems(models.Model):

    name = models.CharField(max_length=500, blank=True)
    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(Bucketlist, related_name="items")
