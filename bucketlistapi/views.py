from django.http.response import Http404
from django.contrib.auth.models import User
from bucketlistapp.models import Bucketlist, BucketlistItem
from bucketlistapi.serializers import BucketlistSerializer, BucketlistItemSerializer, UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class BucketlistView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BucketlistSerializer
    model = Bucketlist

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, format=None):
        """
        Retrieve all the bucketlist for the current user
        """
        bucketlists = Bucketlist.objects.filter(created_by=self.request.user).all()
        serializer = BucketlistSerializer(bucketlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a bucketlist for the current user
        """

        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketListDetailView(APIView):

    @staticmethod
    def get_bucket_object(pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        get a single bucketlist of the authenticated user
        """
        bucketlist = self.get_bucket_object(pk)
        serializer = BucketlistSerializer(bucketlist)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit a single bucket of the authenticated user
        """
        bucketlist = self.get_bucket_object(pk)
        serializer = BucketlistSerializer(bucketlist, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a single bucketlist of the user
        """
        bucketlist = self.get_bucket_object(pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BucketlistItemView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BucketlistItemSerializer
    model = BucketlistItem

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, bucket_id, format=None):
        """
        retrieve all the item in the bucketlist
        :param bucket_id:
        """
        items = BucketlistItem.objects.filter(bucketlist=BucketListDetailView.get_bucket_object(bucket_id)).all()

        serializer = BucketlistSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, bucket_id, format=None):
        """
        Create a single item for a bucketlist
        :param bucket_id:
        """

        bucket = BucketListDetailView.get_bucket_object(bucket_id)

        serializer = BucketlistItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(bucketlist=bucket)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketlistItemDetailView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_bucket_item(bucket_id, item_id):
        try:
            return BucketlistItem.objects.filter(pk=item_id, bucketlist_id=bucket_id).get()

        except BucketlistItem.DoesNotExist:
            return Http404

    def get(self, request, bucket_id, item_id, format=None):
        """
        get a single bucketlist item
        :param bucket_id:
        :param item_id:
        """

        bucketlistitem = self.get_bucket_item(bucket_id, item_id)
        serializer = BucketlistItemSerializer(bucketlistitem)

        return Response(serializer.data)

    def put(self, request, bucket_id, item_id, format=None):
        """
        Update a single bucket item
        :param bucket_id:
        :param item_id:

        :return: serialized data of the item
        """
        bucketlistitem = self.get_bucket_item(bucket_id, item_id)

        serializer = BucketlistItemSerializer(bucketlistitem, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bucket_id, item_id, format=None):

        """
        Delete a single bucket item with the item_id passed
        :param bucket_id:
        :param item_id:
        """
        bucketlistitem = self.get_bucket_item(bucket_id, item_id)

        bucketlistitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    """
    Get a list of all the users in the database with their bucketlist
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer