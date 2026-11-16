import pytest

from pages.dropdown import DropdownPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
class TestDropdown:
    def test_expected_options_are_present(self, class_browser):
        page = DropdownPage(class_browser)
        page.open()

        assert page.options() == [
            "Please select an option",
            "Option 1",
            "Option 2",
        ]

    def test_option_one_can_be_selected(self, class_browser):
        page = DropdownPage(class_browser)
        page.choose("Option 1")

        assert page.selected() == "Option 1"

    def test_option_two_can_be_selected(self, class_browser):
        page = DropdownPage(class_browser)
        page.choose("Option 2")

        assert page.selected() == "Option 2"
