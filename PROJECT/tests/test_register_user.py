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

        # this code then selects the gender filed for male
        gender_field_xpath = '//input[@value="M"]'
        gender_field_elem = self.browser.find_element(By.XPATH, gender_field_xpath)
        gender_field_elem.click()

        # selects the first name field element using xpath
        # then clicks the input field and adds teh name James in it.
        first_name_field_xpath = '//input[@id="FirstName"]'
        first_name_field_elem = self.browser.find_element(By.XPATH, first_name_field_xpath)
        first_name_field_elem.click()
        first_name_field_elem.send_keys('James')

         # selects the last name field element using xpath
        # then clicks the input field and adds the name Willims in it.
        last_name_field_xpath = '//input[@id="LastName"]'
        last_name_field_elem = self.browser.find_element(By.XPATH, last_name_field_xpath)
        last_name_field_elem.click()
        last_name_field_elem.send_keys('Willims')

        # this code randomly generates a random email address
        random_words = ''.join(random.choice(letters) for _ in range(6))
        email = f'{random_words}@testing.com'

        # selects the email field element using xpath
        # then clicks the input field and adds the email address in it.
        email_field_xpath = '//input[@id="Email"]'
        email_field_elem = self.browser.find_element(By.XPATH, email_field_xpath)
        email_field_elem.click()
        email_field_elem.send_keys(email)

        # selects the password field element using xpath
        # then clicks the input field and adds the password in it.
        password_field_xpath = '//input[@id="Password"]'
        password_field_elem = self.browser.find_element(By.XPATH, password_field_xpath)
        password_field_elem.click()
        password_field_elem.send_keys(PASSWORD)

        # selects the confirm password field element using xpath
        #   then clicks the input field and adds the password in it.
        confirm_password_field_xpath = '//input[@id="ConfirmPassword"]'
        confirm_password_field_elem = self.browser.find_element(By.XPATH, confirm_password_field_xpath)
        confirm_password_field_elem.click()
        confirm_password_field_elem.send_keys(PASSWORD)

        self.browser.implicitly_wait(20)

        # selects the register button element using xpath
        # then clicks the input field and adds the password in it.
        register_btn_xpath = '//input[@id="register-button"]'
        register_btn_elem = self.browser.find_element(By.XPATH, register_btn_xpath)
        register_btn_elem.click()



