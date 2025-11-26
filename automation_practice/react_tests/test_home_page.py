from seleniumbase import BaseCase
from react_pages.home_page import HomePage
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestHomePage(BaseCase):

    def setUp(self,  masterqa_mode=False):
        super().setUp()
        self.home_page = HomePage(self)
        self.home_page.open()

    def tearDown(self):
        super().tearDown()


    def test_verify_home_page_title(self):
        # verify that home page title is correct
        self.assert_title("Practice with React | SDET Unicorns Test Site")

    def test_verify_home_page_url(self):
        self.assert_url("https://practice-react.sdetunicorns.com/")

    def test_nav_search_button_with_input_text(self):
        self.click(self.home_page.nav_search_button)
        self.type(self.home_page.nav_search_input, 'Lenovo')
        self.click('.button-search')
        self.assert_text_visible("Showing Results for Lenovo")

    def test_verify_navbar_products_order(self):
        self.home_page.navbar_products_is_in_correct_order()






