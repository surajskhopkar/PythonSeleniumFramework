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

        name.username().send_keys(getData[0])
        email.emailid().send_keys(getData[1])
        password.passWord().send_keys(getData[2])
        checkbox.checkBox().click()
        time.sleep(10)
        submit.submitButton().click()
        time.sleep(2)
        msg = message.successAlert().text
        print(msg)
        assert "Success" in msg

    @pytest.fixture(params=[('Suraj','Suraj@gmail.com','123456'),('Saanvi','Saanvi@gmail.com','123456'),('Joe','Joe@gmail.com','123456')])
    def getData(self,request):
        return request.param


