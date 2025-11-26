from seleniumbase import BaseCase
from config.defaults import HOME_PAGE_URL
from config.defaults import DEMO_PAGE_URL

class HomePage:

    def __init__(self, sb : BaseCase):
        self.expected_nav_links = None
        self.sb = sb

        # selectors
        self.nav_search_button = '.search-active'
        self.nav_search_input = '.search-content form input[placeholder="Search"]'
        self.nav_search_button_after_input = '.button-search'

    # helper method to open home page
    def open(self):
        self.sb.open(HOME_PAGE_URL)

    # helper method to check navbar products is in correct order
    def navbar_products_is_in_correct_order(self):
        self.expected_nav_links = ["Home", "Products", "About Us", "Contact", "Upload"]
        for index, nav in enumerate(self.expected_nav_links, start=1):
            self.sb.assert_text(nav, f'nav li:nth-child({index}) a')




