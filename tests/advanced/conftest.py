import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser(tmp_path):
    options = Options()

    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options.add_experimental_option("prefs", chrome_prefs)
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")

        if browser:
            try:
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot on fail",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass
