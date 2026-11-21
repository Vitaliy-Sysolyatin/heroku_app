import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://the-internet.herokuapp.com/dynamic_controls"


@allure.feature("The Internet")
@allure.story("Dynamic Controls")
@allure.tag("UI", "WebDriverWait", "Dynamic")
@allure.title("Проверка динамического управления элементами")
def test_dynamic_controls(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 10)

    with allure.step("Проверить наличие чекбокса"):
        checkbox = browser.find_element(By.ID, "checkbox")
        assert checkbox.is_displayed()

    with allure.step("Нажать Remove"):
        browser.find_element(
            By.XPATH,
            "//button[text()='Remove']"
        ).click()

    with allure.step("Дождаться сообщения It's gone!"):
        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "It's gone!"
            )
        )

    with allure.step("Дождаться удаления чекбокса"):
        wait.until(
            EC.staleness_of(checkbox)
        )

    with allure.step("Проверить, что поле ввода неактивно"):
        input_field = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#input-example input")
            )
        )
        assert not input_field.is_enabled()

    with allure.step("Нажать Enable"):
        browser.find_element(
            By.XPATH,
            "//button[text()='Enable']"
        ).click()

    with allure.step("Дождаться сообщения It's enabled!"):
        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "It's enabled!"
            )
        )

    with allure.step("Проверить, что поле ввода стало активным"):
        input_field = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#input-example input")
            )
        )
        assert input_field.is_enabled()