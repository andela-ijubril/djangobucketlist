from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from bucketlistapp.models import Bucketlist, BucketlistItem


class BucketListAPPTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(username='jubril', password='issa')
        self.user.set_password('issa')
        self.user.save()
        self.login = self.client.login(username='jubril', password='issa')
        self.bucketlist1 = Bucketlist.objects.create(name='go to paris', created_by=self.user)
        self.bucketlist2 = Bucketlist.objects.create(name='Become a world class developer', created_by=self.user)
        self.item1 = BucketlistItem.objects.create(name='get a passport', bucketlist=self.bucketlist1)
        self.item2 = BucketlistItem.objects.create(name='contribute to open source', bucketlist=self.bucketlist2, done=True)

    def tearDown(self):
        User.objects.all().delete()
        Bucketlist.objects.all().delete()

    def test_user_can_create_a_bucketlist(self):
        self.assertEqual(self.login, True)
        url = reverse("bucketlists")
        data = {"name": "bla bla bla"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_view_bucketlist(self):
        url = reverse("bucketlists")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_edit_a_bucketlist(self):
        url = reverse("update_bucket_list", kwargs={"bucketlist": self.bucketlist1.id})
        data = {"name": "The updated bucketlist"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_delete_a_bucketlist(self):
        url = reverse("update_bucket_list", kwargs={"bucketlist": self.bucketlist1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_create_an_item(self):
        url = reverse("bucketlist_item", kwargs={"bucketlist": self.bucketlist1.id})
        data = {"name": "get a passport"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_view_bucketlistitem(self):
        url = reverse("bucketlist_item", kwargs={"bucketlist": self.bucketlist1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_edit_an_item(self):
        url = reverse("update_bucketlist_item", kwargs={"bucketlist": self.bucketlist1.id, "item": self.item1.id})
        data = {"name": "The updated item"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_delete_an_item(self):
        url = reverse("update_bucketlist_item", kwargs={"bucketlist": self.bucketlist1.id, "item": self.item1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_mark_item_done(self):
        url = reverse("bucketlist_item_status", kwargs={"bucketlist": self.bucketlist1.id, "item": self.item1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_can_unmark_an_item(self):
        url = reverse("bucketlist_item_status", kwargs={"bucketlist": self.bucketlist2.id, "item": self.item2.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

