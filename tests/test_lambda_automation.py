# Running: pytest --capture=no --verbose tests\test_lambda_automation.py

# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
from pages.BaseApp import BasicTest



class Test_URL(BasicTest):
    # Run only this one test from console:
    # pytest -v -k "test_open_url_1" -s tests\test_lambda_automation.py
    def test_open_url_1(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title

        search_text = "LambdaTest"
        search_box = self.driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)
        search_box.submit()

        # Click on the LambdaTest HomePage Link
        title = "LambdaTest Plans and Pricing | 60 Min/Month Freemium Plan"
        lt_link = self.driver.find_element_by_link_text('Pricing')
        lt_link.click()
        assert title == self.driver.title


@pytest.mark.usefixtures("driver_init")
class Basic_Chrome_Test:
    pass

class Test_URL_Chrome(Basic_Chrome_Test):
    @pytest.mark.parametrize("test_input,expected_element_name,expected_text",
                             [("text1", "li6", "text1"), ("text2", "li6",
                                                          "text2")])
    def test_open_url_2(self, test_input, expected_element_name, expected_text):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()

        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == self.driver.title

        email_text_field = self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(test_input)

        self.driver.find_element_by_id("addbutton").click()

        element_name = self.driver.find_element_by_name("li6").get_attribute(
            "name")

        assert element_name == expected_element_name
        assert (expected_text in self.driver.page_source)
