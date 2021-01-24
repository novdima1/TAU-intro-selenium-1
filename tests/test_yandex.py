# python -m pytest -v tests\test_yandex.py
import pytest
from pages.YandexPages import YandexPage

# python -m pytest -v -k "test_yandex_search" -s tests\test_yandex.py
@pytest.mark.yandex
def test_yandex_search(browser):
    yandex_main_page = YandexPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинк" and "Видео" in elements


