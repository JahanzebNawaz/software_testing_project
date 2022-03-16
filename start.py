"""
this file contains list of import of test classes from all the 5 unit test files.
and importedt unittest library to execute and handle the tests.
"""
import unittest
from PROJECT.tests.test_search import TestSearch
from PROJECT.tests.test_add_to_cart import TestAddToCart
from PROJECT.tests.test_remove_from_cart import TestRemoveFromCart
from PROJECT.tests.test_add_search_filters import TestSearchFilter
from PROJECT.tests.test_register_user import TestRegisterUser
from PROJECT.tests.test_add_review import TestAddReview



if __name__ == "__main__":
    """
    this if __name__ == "__main__" is used to run the test cases in the main file.
    this is the Starter script file of the test cases.
    it contains  test_order list which have all the test classses names in order.
    """
    test_order = [
        TestSearch,
        TestAddToCart,
        TestSearchFilter,
        TestRegisterUser,
        TestAddReview
    ]

    # code to change the order of tests, in reverse order 5, 4... 1
    # test_order.reverse()

    # this is the unittest and testloader library to execute and handle the tests.
    loader = unittest.TestLoader()
    
    suite = unittest.TestSuite()
    for test_class in test_order:
        # this for loop is used to add all the test classes in the test_order list to the suite.
        # the reason of adding this code is the explicit order handling of tests cases.
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    # the main testrunner. that executes the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
    



"""
test_add_review (PROJECT.tests.test_add_review.TestAddReview)
Test add review ... ok
test_register_user (PROJECT.tests.test_register_user.TestRegisterUser)
User Registration UnitTest ... ok
test_add_filters_in_search (PROJECT.tests.test_add_search_filters.TestSearchFilter)
Test add filters in search ... ok
test_add_product_to_cart (PROJECT.tests.test_add_to_cart.TestAddToCart)
Test add product to cart ... ok
test_search_book (PROJECT.tests.test_search.TestSearch)
Test search book ... ok

----------------------------------------------------------------------
Ran 5 tests in 43.660s
"""


"""
test_search_book (PROJECT.tests.test_search.TestSearch)
Test search book ... ok
test_add_product_to_cart (PROJECT.tests.test_add_to_cart.TestAddToCart)
Test add product to cart ... ok
test_add_filters_in_search (PROJECT.tests.test_add_search_filters.TestSearchFilter)
Test add filters in search ... ok
test_register_user (PROJECT.tests.test_register_user.TestRegisterUser)
User Registration UnitTest ... ok
test_add_review (PROJECT.tests.test_add_review.TestAddReview)
Test add review ... ok

----------------------------------------------------------------------
Ran 5 tests in 43.933s

"""