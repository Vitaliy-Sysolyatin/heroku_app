import allure

from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/iframe"


@allure.feature("The Internet")
@allure.story("Frames")
@allure.tag("UI", "iFrame")
@allure.title("Проверка работы с iFrame")
def test_iframe(browser):
    browser.get(URL)

    with allure.step("Найти iFrame"):
        frame = browser.find_element(By.ID, "mce_0_ifr")

    with allure.step("Переключиться внутрь iFrame"):
        browser.switch_to.frame(frame)

    with allure.step("Проверить текст внутри iFrame"):
        text = browser.find_element(By.TAG_NAME, "body").text
        assert text == "Your content goes here."

    with allure.step("Вернуться к основному документу"):
        browser.switch_to.default_content()
