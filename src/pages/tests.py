from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        User.objects.create_superuser("admin", "admin@admin.com", "admin")
        
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        # cls.base_url = cls.live_server_url
        cls.verificationErrors = []
        cls.accept_next_alert = True

        super(MySeleniumTests, cls).setUpClass()

        # cls.driver = WebDriver()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('admin')
        self.driver.find_element_by_xpath('//input[@value="Log in"]').click()
        for i in range(30):
            try:
                if "Site administration" == self.driver.find_element_by_css_selector("#content > h1").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        self.driver.implicitly_wait(5)

        # post test
        self.driver.get(self.live_server_url + "/posts/create/")
        self.driver.find_element_by_id("id_title").clear()
        self.driver.find_element_by_id("id_title").send_keys("Test")
        self.driver.find_element_by_id("id_content").clear()
        self.driver.find_element_by_id("id_content").send_keys("# yayaya")
        self.driver.find_element_by_id("id_tags").clear()
        self.driver.find_element_by_id("id_tags").send_keys("okok, 123")
        Select(self.driver.find_element_by_id("id_status")).select_by_visible_text("published")
        self.driver.find_element_by_css_selector("input.btn.btn-default").click()
        for i in range(30):
            try:
                if "yayaya" == self.driver.find_element_by_css_selector("div.post-detail-item > h1").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
