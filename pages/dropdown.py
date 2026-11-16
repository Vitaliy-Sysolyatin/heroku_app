from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    ENDPOINT = "/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def options(self):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        return [option.text for option in select.options]

    def choose(self, text):
        Select(self.driver.find_element(*self.DROPDOWN)).select_by_visible_text(text)

    def selected(self):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        return select.first_selected_option.text
