import allure
import pytest
import logging
from selene import browser, have, be
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--start-maximized")
    browser.config.driver_options = chrome_options
    logging.getLogger("selene").setLevel(logging.ERROR)
    return chrome_options


@allure.title("Open browser and go to Niffler.qa.guru, quit browser after test")
@pytest.fixture(scope="session", autouse=True)
def open_close_browser(setup_browser):
    with allure.step("Open browser and go to Niffler.qa.guru"):
        # browser.config.window_width, browser.config.window_height = 1920, 1080
        browser.open('https://niffler.qa.guru')
    yield
    with allure.step("Close browser"):
        browser.quit()