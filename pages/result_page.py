from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class ResultPage(BasePage):
    """A class representing the Result Page.

    Inherits from BasePage class.

    Class Attributes:
        - Locators on that page.

    """

    SEARCH_RESULTS = (By.TAG_NAME, "cite")

    def __init__(self, driver):
        super().__init__(driver)
        self._results = self.find_search_results()

    def find_search_results(self):
        """Find all element with the provided locator."""
        return (WebDriverWait(self._driver, 10)
                .until(ec.presence_of_all_elements_located(ResultPage.SEARCH_RESULTS)))

    def get_top_three_results(self):
        """Get a list of strings with top three site results."""
        top_three = []
        for result in self._results[:3]:
            top_three.append(result.text)
        return top_three
