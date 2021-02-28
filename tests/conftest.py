import json

import pytest
import selenium.webdriver
# from selenium import webdriver
# Fixture with parameters for browseres

"""
#  This fixture for test_lambda_automation.py
@pytest.fixture(params=["ff"], scope="class")
def driver_init(request):
    if request.param == "chrome":
       web_driver = selenium.webdriver.Chrome()
    if request.param == "ff":
        web_driver = selenium.webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
"""

@pytest.fixture(scope='session')
def config():
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Browser '{config['browser']}' is not supported")

    # Make its calls wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()




# ____________________________________________________________
@pytest.fixture(name='age')
def some_data():
    """Return answer to ultimate question."""
    return 42