from bucketlistapp.models import Bucketlist, BucketlistItem

from rest_framework import serializers
from django.contrib.auth.models import User


class BucketlistItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BucketlistItem
        fields = ('name', 'done', 'created_date')


class BucketlistSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'created_date', 'created_by')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlist')