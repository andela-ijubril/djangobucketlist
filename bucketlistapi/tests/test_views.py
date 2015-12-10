from rest_framework.test import APITestCase, APIClient
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from bucketlistapp.models import Bucketlist,BucketlistItem
from rest_framework.authtoken.models import Token


class BucketListAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='jubril', password='issa')
        self.bucketlist1 = Bucketlist.objects.create(name='go to paris', created_by=self.user)
        self.bucketlist2 = Bucketlist.objects.create(name='Become a world class developer', created_by=self.user)
        self.bucketlist3 = Bucketlist.objects.create(name='Yolo', created_by=self.user)
        self.item1 = BucketlistItem.objects.create(name='get a passport', bucketlist=self.bucketlist1)
        self.item2 = BucketlistItem.objects.create(name='contribute to open source', bucketlist=self.bucketlist2)

        self.token = Token.objects.get(user_id=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self):
        User.objects.all().delete()
        Bucketlist.objects.all().delete()

    def test_can_get_all_users(self):
        url = reverse("all_users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_create_a_bucketlist(self):
        url = reverse("bucket_list")
        data = {"name": "bla bla bla"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_can_view_bucketlist(self):
        url = reverse("bucket_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_can_view_a_bucketlist(self):
        url = reverse("bucketlist_detail", kwargs={"pk": self.bucketlist1.id})
        response = self.client.get(url, )
        self.assertEqual(response.status_code, 200)

    def test_invalid_bucket(self):
        url = reverse("bucketlist_detail", kwargs={"pk": 5})
        response = self.client.get(url, )
        self.assertEqual(response.status_code, 404)

    def test_user_can_edit_a_bucketlist(self):
        url = reverse("bucketlist_detail", kwargs={"pk": self.bucketlist1.id})
        data = {"name": "The updated bucketlist"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_a_bucketlist(self):
        url = reverse("bucketlist_detail", kwargs={"pk": self.bucketlist1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_user_can_create_an_item(self):
        url = reverse("bucketlist_item", kwargs={"bucket_id": self.bucketlist1.id})
        data = {"name": "get a passport"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_can_view_all_item_in_a_bucketlist(self):
        url = reverse("bucketlist_item", kwargs={"bucket_id": self.bucketlist1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_edit_an_item(self):
        url = reverse("item_detail", kwargs={"bucket_id": self.bucketlist1.id, "item_id": self.item1.id})
        data = {"name": "The updated item"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_an_item(self):
        url = reverse("item_detail", kwargs={"bucket_id": self.bucketlist1.id, "item_id": self.item1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

