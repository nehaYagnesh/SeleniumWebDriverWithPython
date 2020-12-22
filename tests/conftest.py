"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    # Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome("C:/Selenium/chromedriver.exe")

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return to webdriver instance for the setup
    yield b

    # Quit the Webdriver instance for the cleanup
    b.quit()
