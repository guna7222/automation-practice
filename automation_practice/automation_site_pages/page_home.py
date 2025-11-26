from seleniumbase import BaseCase
from config.defaults import BASE_URL

class PageHome:

    def __init__(self, sb : BaseCase):
        self.sb = sb

        # selectors
        self.email_field = '#susbscribe_email'
        self.arrow_field = "#subscribe"

    def open(self):
        self.sb.open(BASE_URL)