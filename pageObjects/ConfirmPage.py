from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver


    country_text = (By.ID,"country")
    verify_link_present = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")
    success_msg = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def countryEditBox(self):
        return self.driver.find_element(*ConfirmPage.country_text)

    def verifyLinkPresent(self):
        return self.driver.find_element(*ConfirmPage.verify_link_present)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.success_msg)


