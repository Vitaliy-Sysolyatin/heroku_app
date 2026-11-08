from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class NotificationsPage(BasePage):
    ENDPOINT = "/notification_message_rendered"
    LINK = (By.LINK_TEXT, "Click here")
    MESSAGE = (By.ID, "flash")
    EXPECTED_MESSAGES = (
        "Action successful",
        "Action unsuccesful, please try again",
    )

    def refresh_message(self):
        self.driver.find_element(*self.LINK).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.MESSAGE)
        )

    def message(self):
        return self.driver.find_element(*self.MESSAGE).text
