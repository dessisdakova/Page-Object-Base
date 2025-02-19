from selenium.webdriver.common.by import By

from elements.base_web_element import BaseWebElement
from pages.base_page import BasePage


class SearchPage(BasePage):
    """A class representing the Search Page.

    Inherits from BasePage class.

    Class Attributes:
        - Locators on that page.

    Properties:
        - Elements (represented as instances of BaseWebElement class) to interact with on that page.
    """

    SEARCH_FIELD = (By. CSS_SELECTOR, "textarea[id='sb_form_q']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "label[id='search_icon']")


    @property
    def search_field(self):
        return BaseWebElement(self._driver, SearchPage.SEARCH_FIELD)

    # I can not find a way to click on a <svg> element.
    # Tried using ActionChains, XPATH, element_to_be_clickable
    @property
    def search_button(self):
        return BaseWebElement(self._driver, SearchPage.SEARCH_BUTTON)
