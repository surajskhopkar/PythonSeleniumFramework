import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def capture_screenshot(name):
        driver.get_screenshot_as_file(name)




