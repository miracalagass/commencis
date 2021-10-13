from selenium.webdriver.common.by import By
from TechCrunch.base_page.base_page import BasePage


class HomePage(BasePage):
    AUTHOR_CONTROL = (By.CLASS_NAME, "river-byline__authors")
    IMAGE_CONTROL = (By.CLASS_NAME, "post-block__footer")
    PRODUCTS_LIST = (By.CLASS_NAME, "post-block__title__link")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def latest_control(self):
        assert self.wait_for_element(self.AUTHOR_CONTROL), True
        assert self.wait_for_element(self.IMAGE_CONTROL), True

    def click_random_product(self):
        """Selects random product from the home page and clicks."""
        products = self.wait_for_elements(self.PRODUCTS_LIST)
        random_int = self.random_number(0, (len(products) - 1))
        random_product = products[random_int]
        random_product.click()

