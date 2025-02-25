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
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(options=options)

    # Specify the path to the Chrome binary
    options.binary_location = "/opt/google/chrome/chrome"
    # Point to chromedriver in /usr/local/bin/
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver-linux64"), options=options)
    yield driver
    driver.quit()
