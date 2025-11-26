from automation_practice.config.defaults import CONTACT_PAGE_URL

class ContactPage:

    def __init__(self, sb):
        self.sb = sb

        # selectors
        self.name_input = 'input[placeholder="Name*"]'
        self.email_input = 'input[placeholder="Email*"]'
        self.subject_input = 'input[placeholder="Subject*"]'
        self.message_input = 'textarea[placeholder="Your Message*"]'
        self.submit = '.submit'

    def open(self):
        self.sb.open(CONTACT_PAGE_URL)