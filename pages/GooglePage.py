from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class GoogleSearshLocators:
    GOOGLE_URL = "https://www.google.by/"
    GOOGLE_SEARCH_FIELD = (By.NAME, 'q')
    GOOGLE_SEARCH_BUTTON = (By.NAME, 'btnK')
    GOOGLE_NAVIGATION_BAR = (By.CLASS_NAME, "hide-focus-ring")


class GooglePage(BasePage):

    def open_google_page(self):
        self.driver.get(GoogleSearshLocators.GOOGLE_URL)

    def enter_word(self, word):
        search_field = self.find_element(
            GoogleSearshLocators.GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        # return search_field

    def click_on_the_search_button(self):
        self.find_element(GoogleSearshLocators.GOOGLE_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(GoogleSearshLocators.GOOGLE_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu