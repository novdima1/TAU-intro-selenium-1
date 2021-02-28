"""
Run in parallel:  F:\Дима\_IT Info\tau-selenium-pytest\tau-intro-selenium-py-1
>python -m pytest -n 2
Run with marker: python -m pytest -m intelliflo_login
"""

import pytest
from pages.intelliflo_login import LoginPage


# Pytest parametrization — passing multiple data-items to a single test
PHRASE = [('novdima', 'testpass0')]
@pytest.mark.parametrize('login, password', PHRASE)
@pytest.mark.intelliflo_login
def test_login(browser, login, password):
    search_page = LoginPage(browser)
    search_page.open_login_page()
    search_page.click_login()
    search_page.enter_credentials(login, password)
    #search_page.click_login_btn()
    #search_page.check_recent_clients_widget()

    # search_page.select_client()



# python -m pytest -m learn_fixture
@pytest.mark.learn_fixture
def test_some_data(age):
    """Use fixture return value in a test."""
    assert age == 42
