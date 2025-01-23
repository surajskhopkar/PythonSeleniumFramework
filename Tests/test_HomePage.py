import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        name = HomePage(self.driver)
        email = HomePage(self.driver)
        password = HomePage(self.driver)
        checkbox = HomePage(self.driver)
        submit = HomePage(self.driver)
        message = HomePage(self.driver)

        name.username().send_keys('Selenium')
        email.emailid().send_keys('TestAutomation@gmail.com')
        password.passWord().send_keys('1234567')
        checkbox.checkBox().click()
        time.sleep(10)
        submit.submitButton().click()
        time.sleep(2)
        msg = message.successAlert().text
        print(msg)
        assert "Success" in msg

        # xpath: //tagname[@attribute='value']


