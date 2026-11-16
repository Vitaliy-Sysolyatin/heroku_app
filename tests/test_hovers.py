import pytest

from pages.hovers import HoversPage


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.xfail(
    reason="ссылки View profile на текущей странице ведут на несуществующие профили"
)
def test_profiles_after_hover(browser):
    page = HoversPage(browser)
    page.open()

    expected_names = ["name: user1", "name: user2", "name: user3"]

    for index, expected_name in enumerate(expected_names):
        page.hover(index)
        assert page.name(index) == expected_name

        page.open_profile(index)
        assert browser.current_url.rstrip("/") != page.BASE_URL + "/users/" + str(index + 1)
        page.open()
