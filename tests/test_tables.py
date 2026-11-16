import pytest

from pages.tables import TablesPage


@pytest.mark.advanced
@pytest.mark.regression
def test_first_table_cells(browser):
    page = TablesPage(browser)
    page.open()

    assert page.cell(1, 1, 1) == "Smith"
    assert page.cell(1, 1, 2) == "John"
    assert page.cell(1, 1, 3) == "jsmith@gmail.com"
    assert page.cell(1, 1, 4) == "$50.00"
