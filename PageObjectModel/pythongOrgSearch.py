#Reference - http://selenium-python.readthedocs.io/page-objects.html#

import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import pages
import HTMLTestRunner
import time


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
       

    def test_search_in_python(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = pages.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches()
         #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        time.sleep(5)
        main_page.click_go_button()
        search_results_page = pages.SearchResults(self.driver)
        time.sleep(5)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No Results found"

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    HTMLTestRunner.main()    