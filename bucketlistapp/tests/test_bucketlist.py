from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from bucketlistapp.views import BucketlistItem, Bucketlist


class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='jubril',
            password='password',
        )

    def test_user_can_create_a_bucketlist(self):
        pass

    def test_user_can_delete_a_bucketlist(self):
        pass

    def test_user_can_edit_a_bucketlist(self):
        pass

    def test_user_can_add_an_item_to_a_bucketlist(self):
        pass

    def test_user_can_mark_an_item_as_done(self):
        pass
