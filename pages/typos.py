from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TyposPage(BasePage):
    ENDPOINT = "/typos"
    PARAGRAPH = (By.TAG_NAME, "p")
    VALID_TEXTS = {
        "Sometimes you'll see a typo, other times you won't.",
        "Sometimes you'll see a typo, other times you won,t.",
    }

    def text(self):
        paragraphs = self.driver.find_elements(*self.PARAGRAPH)
        return paragraphs[1].text
