import pytest

from pages.notifications import NotificationsPage


@pytest.mark.advanced
@pytest.mark.regression
def test_notification_message(browser):
    page = NotificationsPage(browser)
    page.open()
    page.refresh_message()

    assert any(
        page.message().startswith(expected)
        for expected in page.EXPECTED_MESSAGES
    )
