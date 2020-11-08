""" https://duckduckgo.com/ """
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL

    URL = "https://duckduckgo.com/"

    # Locators

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')

    # Initializer

    def __init__(self, browser):
        self.brows = browser

    # Interaction Methods

    def get_browser(self):
        return self.brows

    def load(self):
        self.brows.get(self.URL)

    def search(self, phrase):
        search_input = self.brows.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

