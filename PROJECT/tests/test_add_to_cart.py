from .base_test import BaseTestCase
from PROJECT.settings import By


class TestAddToCart(BaseTestCase):

    def test_add_product_to_cart(self):
        """Test add product to cart"""
        self.browser.get(self.website_url)

        # selects the  search field through the xpath and inserts the  value Book 
        # in it and then clicks on the search button
        search_input_xpath = '//input[@id="small-searchterms"]'
        search_btn_elem = self.browser.find_element(By.XPATH, search_input_xpath)
        search_btn_elem.click()
        self.assertCheck(True, search_btn_elem.is_displayed())
        search_btn_elem.send_keys('Book')
        self.browser.implicitly_wait(2)

        # selects the search button through the xpath and clicks on it
        search_btn_xpath = '//input[@class="button-1 search-box-button"]'
        search_btn_elemm = self.browser.find_element(By.XPATH, search_btn_xpath)
        self.assertCheck(True, search_btn_elemm.is_displayed())
        search_btn_elemm.click()

        # selects the product grid through the xpath and clicks on it
        # to check if the results maching the search query.
        product_grid_xpath = '//div[@class="product-grid"]'
        product_grid_elem = self.browser.find_element(By.XPATH, product_grid_xpath)
        self.assertCheck(True, product_grid_elem.is_displayed())
        text = product_grid_elem.text
        words = text.split()
        self.assertCheck(True, 'Book' in words)

        # selects the add to cart button through the xpath and clicks on it
        add_to_cart_btn_xpath = '//input[@value="Add to cart"]'
        add_to_cart_btn_elem = self.browser.find_element(By.XPATH, add_to_cart_btn_xpath)
        self.assertCheck(True, add_to_cart_btn_elem.is_displayed())
        add_to_cart_btn_elem.click()

        # selects the shopping cart icon through the xpath and clicks on it
        # it redirects to the shopping cart page and displays the product added to the cart
        cart_xpath = '//a[@class="ico-cart"]'
        cart_elem = self.browser.find_element(By.XPATH, cart_xpath)
        self.assertCheck(True, cart_elem.is_displayed())
        cart_elem.click()
        self.browser.implicitly_wait(5)
      