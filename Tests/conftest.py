import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj1 = Service(
        '/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
        'chromedriver-mac-arm64/chromedriver')
        driver = webdriver.Chrome(service=service_obj1)

    elif browser_name == "firefox":
        service_obj1 = Service(
            '/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/geckodriver')
        driver = webdriver.Firefox(service=service_obj1)
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/angularpractice')


    ############   Assigning local driver to class driver    ############
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()



