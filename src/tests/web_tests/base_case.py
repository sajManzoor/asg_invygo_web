import pytest
from selenium import webdriver
from configs.selenium_config import SeleniumConfig
from selenium.webdriver.common.by import By
from pages.pages_manager import PageObjectManager
from utils.constants import Constants


class TestBaseCase:
    pass


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.get(SeleniumConfig.BASE_URL)
    yield driver
    driver.quit()
