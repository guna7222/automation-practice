import os.path

from seleniumbase import BaseCase
from automation_practice.config.defaults import BASE_URL

class PageContactUsForm:

    def __init__(self, sb : BaseCase):
        self.sb = sb

        # selectors
        self.home = ".shop-menu li:nth-child(1)"
        self.contact_us_button = ".shop-menu li a[href='/contact_us']"
        self.name = "input[name='name']"
        self.email = "input[name='email']"
        self.subject = "input[name='subject']"
        self.message = "textarea[name='message']"
        self.file = "input[name='upload_file']"
        self.submit_button = "input[name='submit']"
        self.about_us_home = "#form-section a"

    def open(self):
        self.sb.open(BASE_URL)

    #  Enter name, email, subject and message
    def fill_the_form(self):
        self.sb.type(self.name, 'guna')
        self.sb.type(self.email, 'guna@gmail.com')
        self.sb.type(self.subject, 'testing world')
        self.sb.type(self.message, 'include AI in testing')

    # Upload file
    def upload_file(self):
        file_path = 'C://Users//rrgun/PycharmProjects/seleniumbase-exercise/data/some_image.png'
        self.sb.choose_file(self.file, file_path)