from sys import executable

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOp
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@fixture(scope="function")
def browser():
    options = ChromeOp()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-notifications")

    # local runs
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    # container runs
    """
    chrome_binary_path = "/opt/google/chrome/chrome"
    options.binary_location = chrome_binary_path
    """
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)


    # using image for browser
    # driver = webdriver.Remote("http://browser:4444", options=options)
    yield driver
    driver.quit()
