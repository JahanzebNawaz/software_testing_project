from .base_test import BaseTestCase
from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions
from PROJECT.constant import USERNAME, PASSWORD, EMAIL
import random
from string import ascii_uppercase as letters


class TestRegisterUser(BaseTestCase):

    def test_register_user(self):
        """User Registration UnitTest"""
        self.browser.get(self.website_url)

        # this xpath is used to select the login button, and click it to
        # redirect to login page
        register_btn_xpath = '//a[@class="ico-register"]'
        register_btn_elem = self.browser.find_element(By.XPATH, register_btn_xpath)
        register_btn_elem.click()
        self.browser.implicitly_wait(2)

        gender_field_xpath = '//input[@value="M"]'
        gender_field_elem = self.browser.find_element(By.XPATH, gender_field_xpath)
        gender_field_elem.click()

        first_name_field_xpath = '//input[@id="FirstName"]'
        first_name_field_elem = self.browser.find_element(By.XPATH, first_name_field_xpath)
        first_name_field_elem.click()
        first_name_field_elem.send_keys('James')

        last_name_field_xpath = '//input[@id="LastName"]'
        last_name_field_elem = self.browser.find_element(By.XPATH, last_name_field_xpath)
        last_name_field_elem.click()
        last_name_field_elem.send_keys('Willims')

        random_words = ''.join(random.choice(letters) for _ in range(6))
        email = f'{random_words}@testing.com'

        email_field_xpath = '//input[@id="Email"]'
        email_field_elem = self.browser.find_element(By.XPATH, email_field_xpath)
        email_field_elem.click()
        email_field_elem.send_keys(email)

        password_field_xpath = '//input[@id="Password"]'
        password_field_elem = self.browser.find_element(By.XPATH, password_field_xpath)
        password_field_elem.click()
        password_field_elem.send_keys(PASSWORD)

        confirm_password_field_xpath = '//input[@id="ConfirmPassword"]'
        confirm_password_field_elem = self.browser.find_element(By.XPATH, confirm_password_field_xpath)
        confirm_password_field_elem.click()
        confirm_password_field_elem.send_keys(PASSWORD)

        self.browser.implicitly_wait(20)

        register_btn_xpath = '//input[@id="register-button"]'
        register_btn_elem = self.browser.find_element(By.XPATH, register_btn_xpath)
        register_btn_elem.click()



