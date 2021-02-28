"""https://www.intelligent-office.net/nio/Authentication/Login"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.BaseApp import BasePage


class LoginPageLocators:
    URL = "https://tst-05.test.intelliflo.com/nio/authentication/login"
    LOGIN_BTN = (By.CSS_SELECTOR, 'a[title="Login"]')
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN1 = (By.CSS_SELECTOR, 'button[type="submit"]')
    CLIENT = (By.CSS_SELECTOR,
              'a[href="/nio/clientsearch/31106292/redirectfromclientrestore/0"]')
    SKIP_FOR_NOW = (By.PARTIAL_LINK_TEXT, 'Skip for now')
    RECENT_CLIENTS_WIDGET = (By.LINK_TEXT, 'My Recent Clients')

class LoginPage(BasePage):


    # Initializer
    # Implemented in BasePage class

    # def __init__(self, browser):
    #     self.page = browser


    # Interaction Methods

    def open_login_page(self):
        self.driver.get(LoginPageLocators.URL)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BTN).click()

    def enter_credentials(self, login, password):
        login = self.find_element(LoginPageLocators.LOGIN_INPUT).send_keys(login)
        password = self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(
            password)

    def click_login_btn(self):
        btn = self.find_element(LoginPageLocators.LOGIN_BTN1)
        btn.click()
        skip = self.find_element(LoginPageLocators.SKIP_FOR_NOW)
        skip.click()

    def select_client(self):
        client = self.find_element(LoginPageLocators.CLIENT)
        client.click()

    def check_recent_clients_widget(self):
           widget = self.find_element(LoginPageLocators.RECENT_CLIENTS_WIDGET).text
           assert widget == "My Recent Clients1", "No such widget!"





