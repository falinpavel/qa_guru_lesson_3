import allure
import pytest
from selene import browser, be, have


@allure.title("Login in Niffler and logout after test")
@pytest.fixture(scope="function", autouse=True)
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