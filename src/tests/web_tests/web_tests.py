import pytest
from selenium import webdriver
from configs.selenium_config import SeleniumConfig
from selenium.webdriver.common.by import By
from pages.pages_manager import PageObjectManager
from utils.constants import Constants
from tests.web_tests.base_case import TestBaseCase
from tests.web_tests.base_case import browser


class TestBrandFilter(TestBaseCase):

    def test_brand_filter_location(self, browser):
        self.page_manager = PageObjectManager(browser)
        self.page_manager.home_page.explore_cars.click()
        self.page_manager.monthly_subs_page.checkIfMandatoryComponents()
        filter_list = self.page_manager.monthly_subs_page.filter_list

        # brand filter should be at the second position
        brand_filter = filter_list[1]
        brand_filter_text = brand_filter.text
        assert brand_filter_text == Constants.BRANDS_FILTER_LABEL, \
            f"{brand_filter_text} displayed - Expected is {Constants.BRANDS_FILTER_LABEL}"

    def test_brand_filter_select_filter(self, browser):
        self.page_manager = PageObjectManager(browser)
        self.page_manager.home_page.explore_cars.click()
        self.page_manager.monthly_subs_page.checkIfMandatoryComponents()

        brand_filter_element = self.page_manager.monthly_subs_page.filter_list[1]
        brand_filter_element.click()
        filter_option_list = self.page_manager.monthly_subs_page.\
            get_selected_filter_options(brand_filter_element)

        # choose the first filter
        filter_option_list[0].click()
        self.page_manager.monthly_subs_page.press_filter_done_button(brand_filter_element)

        observed_selected_filter = self.page_manager.monthly_subs_page.get_selected_filter_options(brand_filter_element)
        assert observed_selected_filter == brand_filter_element.text, f"Exp - {observed_selected_filter} Obs - " \
                                                                      f"{brand_filter_element.text}"


def test_select_brand_filter(browser):
    page_manager = PageObjectManager(browser)
    page_manager.home_page.explore_cars.click()

    browser.find_element(By.CSS_SELECTOR, ".sc-12f94560-1:nth-child(2) .sc-5ec37f40-2").click()
    browser.find_element(By.CSS_SELECTOR, ".sc-5ec37f40-8:nth-child(3) > .sc-5ec37f40-7").click()
    browser.find_element(By.CSS_SELECTOR, ".sc-5ec37f40-11").click()
    car_list = browser.find_element(By.CSS_SELECTOR, ".sc-e9eba0a1-3.ggQCtb")
    browser.execute_script("arguments[0].scrollIntoView();", car_list)

    link_elements = car_list.find_elements(By.XPATH, "./a")

    for anchor_element in link_elements:
        main_card = anchor_element.find_element(By.CLASS_NAME, "sc-e9eba0a1-4")
        time_avail = main_card.find_element(By.CLASS_NAME, "sc-e9eba0a1-8")
        name = main_card.find_element(By.CLASS_NAME, "sc-e9eba0a1-7")

        bottom = main_card.find_element(By.CLASS_NAME, "sc-e9eba0a1-11")
        year_mileage_price = bottom.find_element(By.CLASS_NAME, "sc-e9eba0a1-13")

        print(time_avail.text)
        print(name.text)
        print(year_mileage_price.text)

def test_brand_filter_options(browser):

    page_manager = PageObjectManager(browser)
    page_manager.home_page.explore_cars.click()
    brand_filter = page_manager.monthly_subs_page



    filter_element = browser.find_element(By.CLASS_NAME, "sc-12f94560-0")
    all_filters = filter_element.find_elements(By.CLASS_NAME,"sc-12f94560-1")

    all_filters[1].click()
    brands_options_div = all_filters[1].find_element(By.CLASS_NAME, "sc-5ec37f40-6")
    brad_options = brands_options_div.find_elements(By.CLASS_NAME,"sc-5ec37f40-8")
    for brand in brad_options:
        print(brand.text)







