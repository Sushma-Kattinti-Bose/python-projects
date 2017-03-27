from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage():
    def login(self, webdriver, username, password):
        driver = webdriver
        facebookUsername = username
        facebookPassword = password
        emailFieldID = "email"
        passFieldID = "pass"
        logingButtonXpath = "//input[@value='Log In']"
        facebookLogoXpath = "//a[contains(@data-testid, 'blue_bar_fb_logo')]"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        logingButtonXpath = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logingButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        logingButtonXpath.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(facebookLogoXpath))
