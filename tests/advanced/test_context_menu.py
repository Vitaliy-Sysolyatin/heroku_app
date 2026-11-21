import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/context_menu"


@allure.feature("The Internet")
@allure.story("Context Menu")
@allure.tag("UI", "ActionChains", "Alert")
@allure.title("Проверка контекстного меню")
def test_context_menu(browser):
    browser.get(URL)

    with allure.step("Найти область контекстного меню"):
        hot_spot = browser.find_element(By.ID, "hot-spot")

    with allure.step("Выполнить правый клик"):
        ActionChains(browser).context_click(hot_spot).perform()

    with allure.step("Проверить текст Alert"):
        alert = browser.switch_to.alert
        assert alert.text == "You selected a context menu"

    with allure.step("Закрыть Alert"):
        alert.accept()
