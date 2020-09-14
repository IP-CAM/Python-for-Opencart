"""
These tests cover adding product to the cart.
"""

from page.homePage import Homepage


def test_basic_home_page(browser):

    home_page = Homepage(browser)

    # Given the home page is displayed
    home_page.load()
    # When the user clicks the [Add Cart] button
    home_page.click_add_button()
