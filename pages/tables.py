from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TablesPage(BasePage):
    ENDPOINT = "/tables"

    def cell(self, table_number, row_number, column_number):
        locator = (
            By.XPATH,
            f"//table[{table_number}]//tbody/tr[{row_number}]/td[{column_number}]",
        )
        return self.driver.find_element(*locator).text
