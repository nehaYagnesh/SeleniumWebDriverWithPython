"""
This module contains shared fixtures
"""
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    # Read the config file 
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert if the values are acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0

    #Return config so it can be used
    return config

@pytest.fixture
def browser(config):

    #Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
         b = selenium.webdriver.Chrome("C:/Selenium/chromedriver.exe")
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome('C:/Selenium/chromedriver.exe',options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return to webdriver instance for the setup
    yield b

    # Quit the Webdriver instance for the cleanup
    b.quit()
