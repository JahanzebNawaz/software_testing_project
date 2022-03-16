import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PROJECT.constant import WEBSITE_URL, LOGOUT_URL, EMAIL, PASSWORD, DRIVER_PATH
from PROJECT.settings import By, Keys
import time


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.website_url = WEBSITE_URL
        self.service = Service(DRIVER_PATH)
        self.browser = webdriver.Chrome(service=self.service)
        self.browser.maximize_window()

    def tearDown(self):
        time.sleep(1)
        self.browser.close()

    def login_user(self):
        """User login UnitTest, test login to account"""
        self.browser.get(self.website_url)

        # this xpath is used to select the login button, and click it to
        # redirect to login page
        login_btn_xpath = '//a[@class="ico-login"]'
        login_btn_elem = self.browser.find_element(By.XPATH, login_btn_xpath)
        login_btn_elem.click()
        self.browser.implicitly_wait(3)

        # this code then selects the email field clicks it,
        #  then enters teh email details.
        email_field_xpath = '//input[@id="Email"]'
        email_field_elem = self.browser.find_element(By.XPATH, email_field_xpath)
        email_field_elem.click()
        email_field_elem.send_keys(EMAIL)

        # then it selects the password fields using XPATH.
        # enters the password for the account.
        password_field_xpath = '//input[@id="Password"]'
        password_field_elem = self.browser.find_element(By.XPATH, password_field_xpath)
        password_field_elem.click()
        password_field_elem.send_keys(PASSWORD)

        # here it selects the login button and then clicks on it.
        # to login the user.
        login_btn_xpath = '//input[@class="button-1 login-button"]'
        login_btn_elem = self.browser.find_element(By.XPATH, login_btn_xpath)
        login_btn_elem.click()

    def logout_user(self):
        # this method logs out the user before closing the browser.
        self.browser.get(LOGOUT_URL)


    def assertCheck(self, message, expected):
        """
        This method is used to check the assertion of the test case.
        """
        self.assertEqual(message, expected)
