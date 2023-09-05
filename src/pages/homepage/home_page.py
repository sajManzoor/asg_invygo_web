from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePageLocators:
    EXPLORE_CARS_BUTTON = (By.CSS_SELECTOR, "div[class='sc-dkrFOg gRGKZq'] a")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.explore_cars = self.find_element(HomePageLocators.EXPLORE_CARS_BUTTON)
        self.mandatoryElements.append(self.explore_cars)
