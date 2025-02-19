from time import sleep

from pytest import mark
from selenium.webdriver import Keys

from pages.result_page import ResultPage
from pages.search_page import SearchPage


def test_open_page(browser):
    page = SearchPage(browser)
    page.open()

    assert "Microsoft Bing" in page.get_title()

def test_entering_search_button(browser):
    test_data = "python"

    page = SearchPage(browser)
    page.open()
    page.search_field.enter_text(test_data)
    sleep(1)
    page.search_field.enter_text(Keys.ENTER)

    assert "search" in page.get_current_url()

@mark.skip(reason="Search results are always different")
def test_results_match_expected(browser):
    test_data = "python"
    expected_results = ["https://www.python.org, https://www.python.org", "https://www.w3schools.com"]

    page = SearchPage(browser)
    page.open()
    page.search_field.enter_text(test_data)
    sleep(1)
    page.search_field.enter_text(Keys.ENTER)

    result_page = ResultPage(browser)
    actual_results = result_page.get_top_three_results()
    for expected in expected_results:
        assert expected in actual_results