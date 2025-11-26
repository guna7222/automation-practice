import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seleniumbase import BaseCase
from react_pages.upload_page import UploadPage


class TestUploadPage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        self.upload_page = UploadPage(self)
        self.upload_page.open()

    def test_single_upload_file(self):
        self.upload_page.upload_single_file()

    def test_multiple_upload_file(self):
        self.upload_page.upload_multiple_file()