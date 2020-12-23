"""
These tests cover DuckDuckGo searches
"""
import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize('phrase',['panda','python','polar bear'])
def test_basic_duckduckgo_search(browser,phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckduckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase in result_page.search_input_value()

    # And the search result links pertains to "panda"
    titles = result_page.result_link_titles()
    matches = [ t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    # (Providing this assertion at the last guarantees that the page title will be ready)
    assert phrase in result_page.title()

     # And the search result title contains "panda"
    assert phrase in result_page.title()