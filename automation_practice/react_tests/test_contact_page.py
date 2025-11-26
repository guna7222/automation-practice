from seleniumbase import BaseCase
from automation_practice.config.defaults import CONTACT_PAGE_URL

class TestContactPage(BaseCase):

    def test_fill_get_in_touch_form(self):
        self.open(CONTACT_PAGE_URL)
        self.type('input[name="name"]', 'John Doe')
        #self.type('input[name="email"]', '