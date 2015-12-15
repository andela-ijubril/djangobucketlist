from django.contrib.auth.models import User
from rest_framework import serializers
from bucketlistapp.models import Bucketlist, BucketlistItem


class BucketlistItemSerializer(serializers.ModelSerializer):
    """
    Bucketlist item serializer
    """
    bucketlist = serializers.ReadOnlyField(source='bucketlist.name')
    class Meta:
        model = BucketlistItem
        fields = ('id', 'name', 'done', 'created_date', 'bucketlist')


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Bucketlist serializer
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=BucketlistItem.objects.all())

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'created_date', 'created_by', 'items')


class UserSerializer(serializers.ModelSerializer):
    bucketlist = serializers.PrimaryKeyRelatedField(many=True, queryset=Bucketlist.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlist')