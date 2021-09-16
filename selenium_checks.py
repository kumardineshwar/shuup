#!/usr/bin/python3

import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options




target_url = "http://34.88.219.177/"


print("########## Running the Selenium Script ##########")


@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield
    driver.close()


@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_tag_name("h1")
    print("########## Checking for Shuup main page ##########")
    assert element.text == "Welcome to Default Shop!"
