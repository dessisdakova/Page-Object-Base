from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOp
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.result_page import ResultPage
from pages.search_page import SearchPage


options = ChromeOp()
options.add_argument("--headless")
options.add_argument("--disable-logging")
options.add_argument("--disable-notifications")

# Not sure if I should use webdriver_manager library or should just initialize the webdriver
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

page = SearchPage(driver)
page.open()
page.search_field.enter_text("python")
page.search_button.click()
result_page = ResultPage(driver)
print(result_page.get_top_three_results())

driver.quit()