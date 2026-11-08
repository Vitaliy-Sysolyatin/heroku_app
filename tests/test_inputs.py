import pytest
from selenium.webdriver.common.keys import Keys

from pages.inputs import InputsPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("number", ["0", "9999", "9.999", "-9999"])
def test_number_can_be_entered(browser, number):
    page = InputsPage(browser)
    page.open()
    page.enter(number)

    assert page.value() == number


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.xfail(reason="Поле number не принимает буквенный ввод")
def test_letters_can_be_entered(browser):
    page = InputsPage(browser)
    page.open()
    page.enter("test")

    assert page.value() == "test"


@pytest.mark.advanced
@pytest.mark.regression
def test_arrow_up_changes_number(browser):
    page = InputsPage(browser)
    page.open()
    page.enter("10")
    page.field().send_keys(Keys.ARROW_UP)

    assert page.value() == "11"


@pytest.mark.advanced
@pytest.mark.regression
def test_arrow_down_changes_number(browser):
    page = InputsPage(browser)
    page.open()
    page.enter("10")
    page.field().send_keys(Keys.ARROW_DOWN)

    assert page.value() == "9"

@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.skipif(
    True,
    reason="Тестирование skipif в рамках бесполезного теста",
)
def test_arrow_down_and_up_changes_number(browser):
    page = InputsPage(browser)
    page.open()
    page.enter("10")
    page.field().send_keys(Keys.ARROW_DOWN)

    assert page.value() == "9"

    page.field().send_keys(Keys.ARROW_UP)

    assert page.value() == "10"