import pytest

from pages.add_remove import AddRemovePage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_add_two_delete_one(browser):
    page = AddRemovePage(browser)
    page.open()

    page.add()
    page.add()
    assert page.delete_count() == 2

    page.delete()
    assert page.delete_count() == 1
