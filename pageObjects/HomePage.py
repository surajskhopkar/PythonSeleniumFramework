from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_alert = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.shop)

    def username(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.name)

    def emailid(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.email)

    def passWord(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.password)

    def checkBox(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.checkbox)

    def submitButton(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.submit)

    def successAlert(self):
        # * so that it treats variable as a tuple
        return self.driver.find_element(*HomePage.success_alert)