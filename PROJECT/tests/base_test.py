import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PROJECT.constant import WEBSITE_URL, LOGOUT_URL, EMAIL, PASSWORD
from PROJECT.settings import By, Keys
import time


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
        # self.addCleanup(self.browser.quit)

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


