from .base_test import BaseTestCase
from PROJECT.settings import By


class TestSearch(BaseTestCase):

    def test_search_book(self):
        """Test search book"""
        self.browser.get(self.website_url)

        # this xpath is used to select the login button, and click it to
        # redirect to login page
        search_input_xpath = '//input[@id="small-searchterms"]'
        search_btn_elem = self.browser.find_element(By.XPATH, search_input_xpath)
        search_btn_elem.click()
        self.assertCheck(True, search_btn_elem.is_displayed())
        search_btn_elem.send_keys('Book')
        self.browser.implicitly_wait(2)

        search_btn_xpath = '//input[@class="button-1 search-box-button"]'
        search_btn_elemm = self.browser.find_element(By.XPATH, search_btn_xpath)
        self.assertCheck(True, search_btn_elemm.is_displayed())
        search_btn_elemm.click()

        product_grid_xpath = '//div[@class="product-grid"]'
        product_grid_elem = self.browser.find_element(By.XPATH, product_grid_xpath)
        self.assertCheck(True, product_grid_elem.is_displayed())
        text = product_grid_elem.text
        words = text.split()
        self.assertCheck(True, 'Book' in words)
      