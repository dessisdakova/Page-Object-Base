from selenium.webdriver.common.by import By

from elements.base_web_element import BaseWebElement
from pages.base_page import BasePage


class SearchPage(BasePage):
    """A class representing the Search Page.

    Inherits from BasePage class.

    Class Attributes:
        - Locators on that page.

    Properties:
        - Elements to interact with on that page.
    """

    SEARCH_FIELD = (By. CSS_SELECTOR, "textarea[id='sb_form_q']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "label[id='search_icon']")

    @property
    def search_field(self):
        return BaseWebElement(self._driver, SearchPage.SEARCH_FIELD)

    @property
    def search_button(self):
        return BaseWebElement(self._driver, SearchPage.SEARCH_BUTTON)
