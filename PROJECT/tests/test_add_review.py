from .base_test import BaseTestCase
from PROJECT.settings import By


class TestAddReview(BaseTestCase):

    def test_add_review(self):
        """Test add review"""
        self.browser.get(self.website_url)
        self.login_user()

        book_menu_xpath = '//a[@href="/books"]'
        book_menu_elem = self.browser.find_element(By.XPATH, book_menu_xpath)
        self.assertCheck(True, book_menu_elem.is_displayed())
        book_menu_elem.click()


        book_xpath = '//a[@href="/computing-and-internet"]'
        book_elem = self.browser.find_element(By.XPATH, book_xpath)
        self.assertCheck(True, book_elem.is_displayed())
        book_elem.click()

        book_review_xpath = '//a[@href="/productreviews/13"]'
        book_review_elem = self.browser.find_element(By.XPATH, book_review_xpath)
        self.assertCheck(True, book_review_elem.is_displayed())
        book_review_elem.click()

        review_title_xpath = '//input[@class="review-title"]'
        review_title_elem = self.browser.find_element(By.XPATH, review_title_xpath)
        review_title_elem.click()
        # self.assertCheck(True, review_title_elem.is_selected())
        review_title_elem.send_keys('Test Review')

        review_text_xpath = '//textarea[@class="review-text"]'
        review_text_elem = self.browser.find_element(By.XPATH, review_text_xpath)
        review_text_elem.click()
        # self.assertCheck(True, review_text_elem.is_selected())
        review_text_elem.send_keys('This is a test review')

        add_review_btn_xpath = '//input[@name="add-review"]' 
        add_review_btn_elem = self.browser.find_element(By.XPATH, add_review_btn_xpath)
        self.assertCheck(True, add_review_btn_elem.is_displayed())
        add_review_btn_elem.click()

        self.logout_user()


