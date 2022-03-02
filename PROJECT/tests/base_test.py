import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PROJECT.constant import WEBSITE_URL, LOGOUT_URL
import time
import pytest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.website_url = WEBSITE_URL
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(
            service=self.service, options=chrome_options
        )
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        time.sleep(1)
        self.browser.get(LOGOUT_URL)
        self.browser.close()

