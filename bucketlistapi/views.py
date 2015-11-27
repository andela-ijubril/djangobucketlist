from django.http.response import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from bucketlistapp.models import Bucketlist, BucketlistItem
from bucketlistapi.serializers import BucketlistSerializer, BucketlistItemSerializer, UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.


# class BucketlistView(generics.ListAPIView):
#
#     model = Bucketlist
#     serializer_class = BucketlistSerializer


class BucketlistView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Bucketlist

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, format=None):
        bucketlists = Bucketlist.objects.filter(created_by=self.request.user).all()
        # bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = BucketlistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketListDetailView(APIView):

    def get_bucket_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bucketlist = self.get_bucket_object(pk)
        serializer = BucketlistSerializer(bucketlist)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bucketlist = self.get_bucket_object(pk)

        serializer = BucketlistSerializer(bucketlist, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bucketlist = self.get_bucket_object(pk)

        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BucketlistItemView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # queryset = Bucketlist.objects.all()
    serializer_class = BucketlistItemSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = BucketlistItem

    def get_bucket_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, format=None):
        items = BucketlistItem.objects.filter(created_by=self.request.user).all()
        # bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):

        bucket = self.get_bucket_object(pk)

        serializer = BucketlistItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(bucketlist=bucket.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BucketlistItemDetailView(generics.ListAPIView):

class BucketlistItemDetailView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_bucket_item(self, pk):
        try:
            return BucketlistItem.objects.filter(bucketlist=pk).get(pk=pk)
        except BucketlistItem.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        bucketlistitem = self.get_bucket_item(pk)
        serializer = BucketlistItemSerializer(bucketlistitem)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bucketlistitem = self.get_bucket_item(pk)

        serializer = BucketlistItemSerializer(bucketlistitem, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bucketlistitem = self.get_bucket_item(pk)

        bucketlistitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer