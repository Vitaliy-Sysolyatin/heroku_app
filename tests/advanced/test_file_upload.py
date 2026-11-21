import allure

from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/upload"


@allure.feature("The Internet")
@allure.story("File Upload")
@allure.tag("UI", "File Upload")
@allure.title("Проверка загрузки файла")
def test_file_upload(browser, tmp_path):
    browser.get(URL)

    with allure.step("Создать тестовый файл"):
        file_path = tmp_path / "upload_test.txt"
        file_path.write_text(
            "Test file for Selenium upload",
            encoding="utf-8"
        )

    with allure.step("Загрузить файл"):
        browser.find_element(
            By.ID,
            "file-upload"
        ).send_keys(str(file_path))

    with allure.step("Нажать Upload"):
        browser.find_element(
            By.ID,
            "file-submit"
        ).click()

    with allure.step("Проверить имя загруженного файла"):
        uploaded_file = browser.find_element(
            By.ID,
            "uploaded-files"
        )

        assert uploaded_file.text == file_path.name
