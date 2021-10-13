from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import random


class BasePage(object):
    """Base class to initialize the base page that will bw called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def wait_for_element(self, locator):
        """wait the element until clickable"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_elements(self, locator):
        """wait the elements until clickable"""
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    @staticmethod
    def random_number(first_value, second_value):
        """
        Return random number between parameters
        param first_value: beginning value of the range
        param second_value: last value of the range
        """
        return random.randint(first_value, second_value)
