from selenium import webdriver
from configs.selenium_config import SeleniumConfig
from pages.pages_manager import PageObjectManager


class TestBaseCase:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(SeleniumConfig.BASE_URL)

    def navigate_to_cars_page(self):
        self.page_manager = PageObjectManager(self.driver)
        self.page_manager.home_page.explore_cars.click()
        self.page_manager.cars_page.checkIfMandatoryComponents()

    def teardown_method(self, method):
        self.driver.quit()





