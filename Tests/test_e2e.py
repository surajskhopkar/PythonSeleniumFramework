import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        logging = self.getLogger()
        homePage = HomePage(self.driver)
        getproductlist = CheckoutPage(self.driver)
        checkoutbutton = CheckoutPage(self.driver)
        finalcheckoutbutton = CheckoutPage(self.driver)
        countryeditBox = ConfirmPage(self.driver)
        verifylinkpresent = ConfirmPage(self.driver)
        checkbox = ConfirmPage(self.driver)
        purchasebutton = ConfirmPage(self.driver)
        successmessage = ConfirmPage(self.driver)

        homePage.shopItems().click()
        logging.info('Getting al the card items')
        items_list_elements = getproductlist.getProductList()

        for element in items_list_elements:
            product_name = element.find_element(By.XPATH, "div/h4/a").text
            if product_name == 'Nokia Edge':
                element.find_element(By.XPATH, "div/button").click()


        checkoutbutton.checkOutButton().click()
        finalcheckoutbutton.finalCheckoutButton().click()

        logging.info('Searching for the country')
        countryeditBox.countryEditBox().send_keys("ind")

        logging.info('Checking if country name is present in the drop-down')
        self.verifyLinkPresent("India")
        verifylinkpresent.verifyLinkPresent().click()
        checkbox.checkBox().click()

        logging.info('Clicking on the purchase button')
        purchasebutton.purchaseButton().click()

        logging.info(successmessage.successMessage())
