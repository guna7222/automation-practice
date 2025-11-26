import os.path

from automation_practice.config.defaults import UPLOAD_PAGE_URL

class UploadPage:
    def __init__(self, sb):
        self.sb = sb

        # selectors
        self.single_file_upload = '.single input'
        self.multiple_file_upload = '.multiple input'


    def open(self):
        self.sb.open(UPLOAD_PAGE_URL)

    def upload_single_file(self):
        file_path = 'C:/Users/rrgun\PycharmProjects/automation_practice/data/sbase_udemy_certificate_jpg.jpg'
        self.sb.choose_file(self.single_file_upload, file_path)

    def upload_multiple_file(self):
        file_path = f'C:/Users/rrgun/PycharmProjects/automation_practice/data/sbase_udemy_certificate_jpg.jpg \n C:/Users/rrgun\PycharmProjects/automation_practice/data/sbase_udemy_certificate_jpg.jpg  '
        self.sb.choose_file(self.multiple_file_upload, file_path)