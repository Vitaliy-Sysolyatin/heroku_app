import pytest

from pages.checkboxes import CheckboxesPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_first_checkbox_can_be_checked(browser):
    page = CheckboxesPage(browser)
    page.open()

    boxes = page.items()
    assert boxes[0].is_selected() is False

    boxes[0].click()
    assert boxes[0].is_selected() is True


@pytest.mark.advanced
@pytest.mark.regression
def test_second_checkbox_can_be_unchecked(browser):
    page = CheckboxesPage(browser)
    page.open()

    boxes = page.items()
    assert boxes[1].is_selected() is True

    boxes[1].click()
    assert boxes[1].is_selected() is False
