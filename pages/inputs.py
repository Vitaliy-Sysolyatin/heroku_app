from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InputsPage(BasePage):
    ENDPOINT = "/inputs"
    INPUT = (By.TAG_NAME, "input")

    def field(self):
        return self.driver.find_element(*self.INPUT)

    def enter(self, value):
        field = self.field()
        field.clear()
        field.send_keys(value)

    def value(self):
        return self.field().get_attribute("value")
