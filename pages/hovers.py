from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HoversPage(BasePage):
    ENDPOINT = "/hovers"
    CARDS = (By.CSS_SELECTOR, ".figure")

    def hover(self, number):
        card = self.driver.find_elements(*self.CARDS)[number]
        image = card.find_element(By.CSS_SELECTOR, "img")
        ActionChains(self.driver).move_to_element(image).perform()

    def name(self, number):
        card = self.driver.find_elements(*self.CARDS)[number]
        return card.find_element(By.CSS_SELECTOR, "h5").text

    def open_profile(self, number):
        card = self.driver.find_elements(*self.CARDS)[number]
        card.find_element(By.CSS_SELECTOR, "a").click()
