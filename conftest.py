import allure
from selene import browser, have, be
import pytest


@allure.title("Open browser and go to Niffler.qa.guru, quit browser after test")
@pytest.fixture(scope="session", autouse=True)
def browser_fixture():
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.open('https://niffler.qa.guru')
    yield
    browser.quit()


@allure.title("Login in Niffler and logout after test")
@pytest.fixture(scope="session", autouse=True)
def login_and_logout_fixture(browser_fixture):
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345')
    browser.element('button[type="submit"]').click()
    yield
    browser.element('button[aria-haspopup]').should(be.in_dom).click()
    elements = browser.all('li[role="menuitem"]')
    elements[3].should(be.visible).click()
    browser.element('button.css-1v1p78s[type="button"]').click()