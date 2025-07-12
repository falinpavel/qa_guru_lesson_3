from selene import browser, be, have
import allure


@allure.title("Search spending on the main page Niffler")
def test_search_spending(login_and_logout_fixture):
    browser.element('input[placeholder="Search"]').type('test123')