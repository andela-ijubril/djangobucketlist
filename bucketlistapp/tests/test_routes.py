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

    def test_user_can_reach_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_index_is_returned(self):
        match = resolve('/')
        self.assertEqual(match.url_name, 'index')

    def test_can_login(self):
        response = self.client.post('/login', {
            'username': 'jubril',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)

    def test_can_register(self):
        response = self.client.post('/register', {
            'username': 'golden',
            'password': 'abiodun',
            'password_conf': 'abiodun',
            'email': 'abiodun.shuaib@andela.com'
        })
        self.assertEqual(response.status_code, 302)