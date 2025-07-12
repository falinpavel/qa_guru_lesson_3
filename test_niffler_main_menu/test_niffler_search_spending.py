from selene import browser, be, have
import allure


@allure.title("Search spending on the main page Niffler")
def test_search_spending(login_and_logout):
    with allure.step("Search spending, fill field and press Enter"):
        browser.element('canvas[role="img"]').should(be.visible)
        browser.element('input[placeholder="Search"]').should(be.visible).click().type('test123').press_enter()
    with allure.step("Check field is`t empty, and visible text 'There are no spendings'"):
        browser.element('input[placeholder="Search"]').should(have.value('test123'))
        browser.element('//p[text()]').should(have.text('There are no spendings'))