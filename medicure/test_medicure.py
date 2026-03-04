from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MedicureTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homepage_title(self):
        self.driver.get(self.live_server_url)
        time.sleep(2)
        self.assertEqual("MediCure - AI-Powered Healthcare", self.driver.title)
    def tearDown(self):
        self.driver.quit()