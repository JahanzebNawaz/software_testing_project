from .base_test import BaseTestCase
from PROJECT.settings import By


class TestRemoveFromCart(BaseTestCase):

    def test_remove_product_to_cart(self):
        """Test remove product to cart"""
        self.browser.get(self.website_url)

        # through the xpath of menus it selects the books menu
        # and then clicks the element to enter the text.
        book_menu_xpath = '//a[@href="/books"]'
        book_menu_elem = self.browser.find_element(By.XPATH, book_menu_xpath)
        self.assertCheck(True, book_menu_elem.is_displayed())
        book_menu_elem.click()

        # it then adds the book to the cart through selecting the element through the xpath
        add_to_cart_btn_xpath = '//input[@value="Add to cart"]'
        add_to_cart_btn_elem = self.browser.find_element(By.XPATH, add_to_cart_btn_xpath)
        self.assertCheck(True, add_to_cart_btn_elem.is_displayed())
        add_to_cart_btn_elem.click()

        # selects the cart menu and clicks on it to redirect the page to the cart page.
        cart_xpath = '//a[@class="ico-cart"]'
        cart_elem = self.browser.find_element(By.XPATH, cart_xpath)
        self.assertCheck(True, cart_elem.is_displayed())
        cart_elem.click()
        self.browser.implicitly_wait(5)

        # this selects the remove button through the xpath and clicks on it
        # to remove the product from the cart.
        remove_btn_xpath = '//input[@name="removefromcart"]'
        remove_btn_elem = self.browser.find_element(By.XPATH, remove_btn_xpath)
        self.assertCheck(True, remove_btn_elem.is_displayed())
        remove_btn_elem.click()
        self.assertCheck(True, remove_btn_elem.is_selected())

        # this selects the update cart button throught the xpath of the button
        # and it then clicks on it to perform the update.
        update_cart_btn_xpath = '//input[@name="updatecart"]'
        update_cart_btn_elem = self.browser.find_element(By.XPATH, update_cart_btn_xpath)
        self.assertCheck(True, update_cart_btn_elem.is_displayed())
        update_cart_btn_elem.click()
        self.browser.implicitly_wait(5)
