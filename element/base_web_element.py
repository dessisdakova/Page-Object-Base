from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseWebElement:
    """A class representing a Web Element.

    It has the most common actions for interacting with a web element.

    Instance Attributes:
        - _driver (WebDriver) - A WebDriver instance.
        - _locator (tuple) - The locator of the element.
        - _web_element (WebElement) - Holds the element itself.

    """

    def __init__(self, driver: webdriver.Chrome, locator: tuple[str, str]):
        """Initialize an instance of BaseWebElement.

        :param driver: A WebDriver instance.
        :param locator: A tuple containing the locator. Example: (By.ID, 'foo')
        """
        self._driver = driver
        self._locator = locator

        self._web_element = self.find()

    def find(self) -> WebElement:
        """Find the element using explicit wait and
        assign it to instance attribute '_web_element'."""
        return (WebDriverWait(self._driver, 10)
                .until(ec.presence_of_element_located(self._locator)))

    def click(self) -> None:
        """Click on the element."""
        (WebDriverWait(self._driver, 10)
         .until(ec.element_to_be_clickable(self._locator)).click())

    def get_text(self) -> str:
        """Retrieve the text of the element."""
        return self._web_element.text

    def enter_text(self, text: str) -> None:
        """Enter text to the element.

        :param text: A string representing the text.
        """
        self._web_element.send_keys(text)
