
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seleniumbase import BaseCase
from automation_practice.react_pages.about_us_page import AboutUsPage


class TestAboutUsPage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        self.about_us_page = AboutUsPage(self)
        self.about_us_page.open()

    # assert_equal(expected, actual, msg=None)
    def test_verify_who_are_we_is_visible(self):
        # Verify that 'Who are we?' is visible
        actual_text = self.get_text('h5')
        self.assert_equal(actual_text, "Who Are We", "Who are we text is not visible")

    # assert_true(expr, msg=None)
    def test_breadcrumb_is_visible(self):
        # Verify that breadcrumb is visible
        is_breadcrumb_visible = self.is_element_visible(self.about_us_page.breadcrumb)
        self.assert_true(is_breadcrumb_visible, "Breadcrumb is not visible")




