from seleniumbase import BaseCase
from automation_site_pages.page_home import PageHome

class TestHomePage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        self.home_page = PageHome(self)
        self.home_page.open()

    # don't require any teardown for now

    def test_verify_subscribe_in_home_page(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        self.assert_text_visible("Home")

        # Scroll down to footer
        self.scroll_to_bottom()

        # Verify text 'SUBSCRIPTION'
        self.assert_text_visible('SUBSCRIPTION')

        # Enter email address in input and click arrow button
        self.type(self.home_page.email_field, "test@gmail.com")
        self.click(self.home_page.arrow_field)

        #  Verify success message 'You have been successfully subscribed!' is visible
        self.assert_text_visible('You have been successfully subscribed!')