import os

import pytest

from pages.typos import TyposPage

SKIP_TYPO_RELOAD = os.getenv("SKIP_TYPO_RELOAD") == "1"


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_paragraph_has_expected_text(browser):
    page = TyposPage(browser)
    page.open()

    assert page.text() in page.VALID_TEXTS
