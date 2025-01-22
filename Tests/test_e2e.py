import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        items_list_elements = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        print(items_list_elements)
        for element in items_list_elements:
            product_name = element.find_element(By.XPATH, "div/h4/a").text
            if product_name == 'Nokia Edge':
                element.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text)


