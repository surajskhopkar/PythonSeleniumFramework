from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver


    productList = (By.XPATH,"//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkoutButton = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    finalcheckoutButton = (By.CSS_SELECTOR,"button[class*='btn-success']")

    def getProductList(self):
        return self.driver.find_elements(*CheckoutPage.productList)

    def getProductName(self):
        return self.driver.find_element(*CheckoutPage.productName)

    def checkOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def finalCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.finalcheckoutButton)



