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
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
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


@allure.title("Login in Niffler and logout after test")
@pytest.fixture(scope="session", autouse=True)
def login_and_logout(open_close_browser):
    with allure.step("Login in Niffler"):
        browser.element('input[name="username"]').type('stas')
        browser.element('input[name="password"]').type('12345')
        browser.element('button[type="submit"]').click()
        browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    yield
    with allure.step("Logout from Niffler"):
        browser.element('button[aria-haspopup]').should(be.visible).click()
        browser.element('//li[@role="menuitem"][contains(text(), "Sign out")]').should(be.visible).click()
        browser.element('button.css-1v1p78s[type="button"]').click()
