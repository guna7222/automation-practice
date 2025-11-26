from seleniumbase import BaseCase
from automation_practice.config.defaults import CONTACT_PAGE_URL
from parameterized import parameterized
from automation_practice.react_pages.contact_page import ContactPage

class TestContactPage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        self.contact_page = ContactPage(self)
        self.open(CONTACT_PAGE_URL)

    @parameterized.expand([
        ("John Doe", "JohnDoe@gmail.com", "Testing", "Learn AI and ML"),
        ("Andrei", "Andrei@gmail.com", "SDET", "SDET Unicorns are great" ),
    ])
    def test_fill_get_in_touch_form(self, name, email, subject, message ):
        self.assert_text_visible("Get In Touch")
        self.type(self.contact_page.name_input, name)
        self.type(self.contact_page.email_input, email)
        self.type(self.contact_page.subject_input, subject)
        self.type(self.contact_page.message_input, message)
        self.click(self.contact_page.submit)




