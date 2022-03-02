from .base_test import BaseTestCase
from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions
from PROJECT.constant import USERNAME, PASSWORD, EMAIL


class TestLoginUser(BaseTestCase):

    def test_login_user(self):
        """User login UnitTest, test login to account"""
        self.browser.get(self.website_url)
