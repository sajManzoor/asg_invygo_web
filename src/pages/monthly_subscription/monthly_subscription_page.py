from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MonthlySubscriptionLocators:
    FILTER_PANEL = (By.CLASS_NAME, "sc-12f94560-0")
    FILTER_LIST = (By.CLASS_NAME, "sc-12f94560-1")
    FILTER_OPTIONS_DIV = (By.CLASS_NAME, "sc-5ec37f40-6")
    FILTER_OPTION_LIST = (By.CLASS_NAME, "sc-5ec37f40-8")
    FILTER_DONE_BUTTON = (By.CLASS_NAME, "sc-5ec37f40-11")
    FILTER_SELECTED_OPTION_LABEL = (By.CLASS_NAME, "sc-5ec37f40-3")



class MonthlySubscriptionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_panel = self.find_element(MonthlySubscriptionLocators.FILTER_PANEL)
        self.filter_list = self.filter_panel.find_elements(*MonthlySubscriptionLocators.FILTER_LIST)

        self.mandatoryElements.append(self.filter_panel)

    def get_selected_filter_options(self, element):
        selected_filter = element.find_element(*MonthlySubscriptionLocators.FILTER_OPTIONS_DIV)
        filter_options = selected_filter.find_element(*MonthlySubscriptionLocators.FILTER_OPTION_LIST)
        return filter_options

    def press_filter_done_button(self, element):
        done_button = element.find_element(*MonthlySubscriptionLocators.FILTER_DONE_BUTTON)
        done_button.click()

    def get_selected_filter_option_label(self, element):
        selected_option_label = element.find_element(*MonthlySubscriptionLocators.FILTER_SELECTED_OPTION_LABEL)
        return selected_option_label
