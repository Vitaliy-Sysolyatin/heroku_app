from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    ENDPOINT = "/checkboxes"
    CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")

    def items(self):
        return self.driver.find_elements(*self.CHECKBOX)
