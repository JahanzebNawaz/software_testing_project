import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PROJECT.constant import WEBSITE_URL, LOGOUT_URL
import time
import os


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.website_url = WEBSITE_URL
        chrome_options = Options()
        # chrome_options.binary_location = '/usr/bin/google-chrome'
        chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--remote-debugging-port=9222")
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(
            service=self.service,
            options=chrome_options
        )
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        time.sleep(1)
        self.browser.get(LOGOUT_URL)
        self.browser.close()

