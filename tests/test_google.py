import pytest
from pages.GooglePage import GooglePage
import time

# python -m  pytest -v -k "test_google_search" -s tests\test_google.py
@pytest.mark.parametrize("word", ["Hello", "Hella"])
def test_google_search(browser, word):
    google_main_page = GooglePage(browser)\
        .open_google_page()\
        .enter_word(word)\
        .click_on_the_search_button()
    elements = google_main_page.check_navigation_bar()
    assert "Картинк" and "Видео" in elements

