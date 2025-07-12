from selene import browser, be, have
import allure


@allure.title("Search spending on the main page Niffler, ")
def test_successful_search_spending(login_and_logout):
    with allure.step("Search spending, fill field and press Enter, expected result - show search result"):
        browser.element('canvas[role="img"]').should(be.visible)
        browser.element('input[placeholder="Search"]').should(be.visible).click().type('sweets').press_enter()
    with allure.step("Check result of search, should be visible record with 'sweets'"):
        browser.element('input[placeholder="Search"]').should(have.value('sweets'))
        browser.all('//span[text()="sweets"]').should(have.size_greater_than(0))


@allure.title("Unsuccessfully search spending on the main page Niffler, expected result: 'There are no spendings'")
def test_unsuccessful_search_spending(login_and_logout):
    with allure.step("Search spending, fill field and press Enter"):
        browser.element('canvas[role="img"]').should(be.visible)
        browser.element('input[placeholder="Search"]').should(be.visible).click().type('test123').press_enter()
    with allure.step("Check field is`t empty, and visible text 'There are no spendings'"):
        browser.element('input[placeholder="Search"]').should(have.value('test123'))
        browser.element('//p[text()]').should(have.text('There are no spendings'))
