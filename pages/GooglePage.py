from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    class GoogleSearshLocators:
        GOOGLE_URL = "https://www.google.by/"
        GOOGLE_SEARCH_FIELD = (By.NAME, 'q')
        GOOGLE_SEARCH_BUTTON = (By.NAME, 'btnK')
        GOOGLE_NAVIGATION_BAR = (By.CLASS_NAME, "hide-focus-ring")

    def open_google_page(self):
        self.driver.get(self.GoogleSearshLocators.GOOGLE_URL)
        return self

    def enter_word(self, word):
        search_field = self.find_element(
            self.GoogleSearshLocators.GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return self

    def click_on_the_search_button(self):
        self.find_element(self.GoogleSearshLocators.GOOGLE_SEARCH_BUTTON,time=2).click()
        return self

    def check_navigation_bar(self):
        all_list = self.find_elements(self.GoogleSearshLocators.GOOGLE_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu