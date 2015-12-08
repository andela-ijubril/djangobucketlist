from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from bucketlistapp.models import Bucketlist, BucketlistItem


class BucketListAPPTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(username='jubril', password='issa')
        self.login = self.client.login(username='jubril', password='issa')
        self.bucketlist1 = Bucketlist.objects.create(name='go to paris', created_by=self.user)
        self.bucketlist2 = Bucketlist.objects.create(name='Become a world class developer', created_by=self.user)
        self.item1 = BucketlistItem.objects.create(name='get a passport', bucketlist=self.bucketlist1)
        self.item2 = BucketlistItem.objects.create(name='contribute to open source', bucketlist=self.bucketlist2)

    def tearDown(self):
        User.objects.all().delete()
        Bucketlist.objects.all().delete()

    def test_user_can_create_a_bucketlist(self):
        url = reverse("bucketlistapp")
        data = {"name": "bla bla bla"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_view_bucketlist(self):
        url = reverse("bucketlistapp")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_edit_a_bucketlist(self):
        url = reverse("update_bucket_list", kwargs={"bucket_id": self.bucketlist1.id})
        data = {"name": "The updated bucketlist"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 302)
