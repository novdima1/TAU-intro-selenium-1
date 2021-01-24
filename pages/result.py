"""https://duckduckgo.com/?q=result"""
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    # Locators

    SEARCH_INPUT = (By.ID, 'search_form_input')
    RESULT_LINKS = (By.CLASS_NAME, 'result__a')

    # Initializer

    def __init__(self, browser):
        self.brows = browser

    # Interaction Methods

    def result_link_titles(self):
        links = self.brows.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]

        return titles

    def search_input_value(self):
        search_input = self.brows.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.brows.title

    def print_info(self):
        print('Value:', self.brows.find_element(
            *self.SEARCH_INPUT).get_attribute('value'))

