from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddRemovePage(BasePage):
    ENDPOINT = "/add_remove_elements/"
    ADD = (By.XPATH, "//button[text()='Add Element']")
    DELETE = (By.XPATH, "//button[text()='Delete']")

    def add(self):
        self.driver.find_element(*self.ADD).click()

    def delete(self):
        self.driver.find_element(*self.DELETE).click()

    def delete_count(self):
        return len(self.driver.find_elements(*self.DELETE))
