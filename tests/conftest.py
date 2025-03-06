import os
import signal
from sys import executable

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOp
from selenium.webdriver.firefox.options import Options as FireFoxOp
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@fixture(scope="function")
def browser():
    options = ChromeOp()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    yield driver

    driver.close()
    driver.quit()
