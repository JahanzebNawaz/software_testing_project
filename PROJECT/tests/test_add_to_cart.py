from .base_test import BaseTestCase
from PROJECT.settings import By


class TestAddToCart(BaseTestCase):

    def test_add_product_to_cart(self):
        """Test add product to cart"""
        self.browser.get(self.website_url)

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


        add_to_cart_btn_xpath = '//input[@value="Add to cart"]'
        add_to_cart_btn_elem = self.browser.find_element(By.XPATH, add_to_cart_btn_xpath)
        self.assertCheck(True, add_to_cart_btn_elem.is_displayed())
        add_to_cart_btn_elem.click()

        cart_xpath = '//a[@class="ico-cart"]'
        cart_elem = self.browser.find_element(By.XPATH, cart_xpath)
        self.assertCheck(True, cart_elem.is_displayed())
        cart_elem.click()
        self.browser.implicitly_wait(5)
      