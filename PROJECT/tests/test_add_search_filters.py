from .base_test import BaseTestCase
from PROJECT.settings import By


class TestSearchFilter(BaseTestCase):

    def test_add_filters_in_search(self):
        """Test add filters in search"""
        self.browser.get(self.website_url)

        book_menu_xpath = '//a[@href="/books"]'
        book_menu_elem = self.browser.find_element(By.XPATH, book_menu_xpath)
        self.assertCheck(True, book_menu_elem.is_displayed())
        book_menu_elem.click()

        order_by_xpath = '//select[@id="products-orderby"]'
        order_by_elem = self.browser.find_element(By.XPATH, order_by_xpath)
        self.assertCheck(True, order_by_elem.is_displayed())
        order_by_elem.click()

        order_by_a_z_xpath = '//option[@value="http://demowebshop.tricentis.com/books?orderby=5"]'
        order_by_a_z_elem = self.browser.find_element(By.XPATH, order_by_a_z_xpath)
        self.assertCheck(True, order_by_a_z_elem.is_displayed())
        order_by_a_z_elem.click()
        self.browser.implicitly_wait(5)

        order_by_pag_size_xpath = '//select[@id="products-pagesize"]'
        order_by_pag_size_elem = self.browser.find_element(By.XPATH, order_by_pag_size_xpath)
        self.assertCheck(True, order_by_pag_size_elem.is_displayed())
        order_by_pag_size_elem.click()

        order_by_page_size_xpath = '//option[@value="http://demowebshop.tricentis.com/books?orderby=5&pagesize=12"]'
        order_by_page_size_elem = self.browser.find_element(By.XPATH, order_by_page_size_xpath)
        self.assertCheck(True, order_by_page_size_elem.is_displayed())
        order_by_page_size_elem.click()
        self.browser.implicitly_wait(5)


        order_by_price_xpath = '//a[@href="http://demowebshop.tricentis.com/books?orderby=5&pagesize=12&price=-25"]'
        order_by_price_elem = self.browser.find_element(By.XPATH, order_by_price_xpath)
        self.assertCheck(True, order_by_price_elem.is_displayed())
        order_by_price_elem.click()
        self.browser.implicitly_wait(5)
