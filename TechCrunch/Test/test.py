from selenium import webdriver
from TechCrunch.Pages.home_page import HomePage
import unittest


class TestTechCrunch(unittest.TestCase):
    """Test case is:
        1. Go to website
    """

    driver = webdriver
    website = "https://techcrunch.com/"

    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome("/home/mirac-aladag/Desktop/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.HomePage = HomePage(self.driver)

    def test_TechChrunch(self):
        self.HomePage.latest_control()
        self.HomePage.click_random_product()

    @classmethod
    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
