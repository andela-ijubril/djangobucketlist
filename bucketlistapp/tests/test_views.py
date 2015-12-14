from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BucketAppFunctionalityTestCase(StaticLiveServerTestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_bucketlistapp(self):
        self.browser.get(self.live_server_url)

        # Assert that index page was reached
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Sign In', body.text)

        # Assert that login was successful
        self.browser.find_element_by_name('username').send_keys('uzo')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('uzo')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Logged in as uzo', body.text)

        # Add a bucketlist
        bucket_field = self.browser.find_element_by_id('id_name')
        bucket_field.send_keys('My new bucket')
        bucket_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('My new bucket', body.text)

        # Add an item
        self.browser.find_element_by_link_text('My new bucket').click()
        item_field = self.browser.find_element_by_id('id_name')
        item_field.send_keys('my new item')
        item_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('my new item', body.text)

        # Logout
        self.browser.find_element_by_link_text('Logout').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Sign In', body.text)
