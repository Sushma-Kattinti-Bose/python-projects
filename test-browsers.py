"""
This is a selenium test case.
"""
import unittest
import HTMLTestRunner
from login import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestChrome(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
    
    def test_login_chrome(self):
        page = LoginPage()
        page.login(self.driver, "xxxxx@yahoo.co.in","xxxxx!")

    def tearDown(self):
        self.driver.quit()

# class TestFirefox(unittest.TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.facebook.com/")
    
#     def test_login_firefox(self):
#         page = LoginPage()
#         page.login(self.driver, "xxxxx@yahoo.co.in","xxxxx!")

#     def tearDown(self):
#         self.driver.quit()

if __name__ == '__main__':
    HTMLTestRunner.main()