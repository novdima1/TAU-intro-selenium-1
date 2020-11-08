"""
These tests cover DuckDuckGo searches.
Run:  F:\Дима\_IT Info\tau-selenium-pytest\tau-intro-selenium-py-1>python -m pytest -n 2
"""

import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


# Pytest parametrization — passing multiple data-items to a single test
PHRASE = [('leo', 'pard'), ('li', 'on')]
@pytest.mark.parametrize('phrase1, phrase2', PHRASE)
def test_basic_duckduckgo_search(browser, phrase1, phrase2):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = phrase1 + phrase2
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result title contains "panda"
    assert phrase in result_page.title()

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    result_page.print_info()