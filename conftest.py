""" MODULARIZED PYTEST FIXTURE TO RE-USE ON THE TESTS """

import pytest
import os

CHROME_DRIVER = os.getenv('CHROME_DRIVER_PATH', 'drivers/chromedriver')

# BROWSER SELECTION
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome-headless", help="Please select the browser you wish to use.")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        # RUNNING NORMAL
        global driver
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    elif browser == 'chrome-headless':
        # RUNNING HEADLESS
        options = Options()
        options.headless = True
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER)

    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print('\n Test is finished.')