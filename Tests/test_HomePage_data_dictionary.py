import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        name = HomePage(self.driver)
        email = HomePage(self.driver)
        password = HomePage(self.driver)
        checkbox = HomePage(self.driver)
        submit = HomePage(self.driver)
        message = HomePage(self.driver)

        name.username().send_keys(getData["firstname"])
        email.emailid().send_keys(getData["email"])
        password.passWord().send_keys(getData["password"])
        checkbox.checkBox().click()
        time.sleep(10)
        submit.submitButton().click()
        time.sleep(2)
        msg = message.successAlert().text
        print(msg)
        assert "Success" in msg
        self.driver.refresh()

    @pytest.fixture(params=[{"firstname":"John","email":"john@gmail.com","password":"12345"},{"firstname":"David","email":"david@gmail.com","password":"12345"}])
    def getData(self,request):
        return request.param


