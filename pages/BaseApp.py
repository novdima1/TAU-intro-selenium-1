import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.mark.usefixtures("driver_init")
class BasePage:

    def __init__(self, driv):
        self.driver = driv

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).\
            until(EC.presence_of_element_located(locator),
                  message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).\
            until(EC.presence_of_all_elements_located(locator),
                  message=f"Can't find elements by locator {locator}")