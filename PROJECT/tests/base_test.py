import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PROJECT.constant import WEBSITE_URL, LOGOUT_URL
import time
import pytest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.website_url = WEBSITE_URL
        self.browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        time.sleep(3)
        self.browser.get(LOGOUT_URL)
        self.browser.close()

