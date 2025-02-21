from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """A class representing a Page.

    It has common action that can be performed on any page.

    Instance Attributes:
        - _driver (WebDriver) - A webdriver instance used to navigate the page.
        - _url (str) - The URL of the page.
    """

    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver
        self._url = "https://www.bing.com/"

    def open(self) -> None:
        """Open the page."""
        self._driver.get(self._url)
        # Wait for the entire page to load.
        (WebDriverWait(self._driver, 10)
         .until(ec.presence_of_element_located((By.ID, "bnp_container"))))

    def get_title(self) -> str:
        """Retrieve the page's title as string."""
        return self._driver.title

    def get_current_url(self) -> str:
        """Retrieve the driver's current url as string."""
        return self._driver.current_url
