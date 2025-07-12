from selene import browser, be, have
import allure


@allure.title("Search spending on the main page Niffler")
def test_search_spending(login_and_logout_fixture):
    with allure.step("Search spending, fill field and press Enter"):
        browser.element('input[placeholder="Search"]').should(be.visible)
        browser.element('input[placeholder="Search"]').click().type('test123').press_enter()
        browser.element('//p[text()]').should(have.text('There are no spendings'))