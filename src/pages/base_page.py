# base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.mandatoryElements = []

    def wait_for_element(self, by, value, timeout=10):
        if self.is_mobile_test():
            wait = AppiumWebDriverWait(self.driver, timeout)
            wait.until(AppiumEC.presence_of_element_located((by, value)))
        else:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        self.wait_for_element(by, value)
        self.driver.find_element(by, value).click()

    # Other common functions and utility methods

    def is_mobile_test(self):
        # Add logic to determine if the test is mobile or web
        # For example, based on desired capabilities or test configuration
        pass

    def find_element_by_css_selector(self, selector):
        """Finds an element by CSS selector."""
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def find_elements_by_css_selector(self, selector):
        """Finds all elements by CSS selector."""
        return self.driver.find_elements_by_css_selector(selector)

    def find_element(self, selector):
        """Finds all elements by CSS selector."""
        by, value = selector
        return self.driver.find_element(by, value)

    def find_elements(self, selector):
        """Finds all elements by CSS selector."""
        by, value = selector
        return self.driver.find_elements(by, value)

    def enter_text(self, element, text):
        """Enters text into an element."""
        element.send_keys(text)

    def click_button(self, element):
        """Clicks on a button."""
        element.click()

    def select_option(self, element, option):
        """Selects an option from a dropdown."""
        element.find_element_by_css_selector("[value='{}']".format(option)).click()


    def checkIfMandatoryComponents(self):
        try:
            # Use WebDriverWait to wait for elements to be present
            for element in self.mandatoryElements:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element))
            return True  # All elements are present
        except:
            return False  # At least one element is missing
