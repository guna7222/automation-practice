from config.defaults import ABOUT_US_PAGE_URL

class AboutUsPage:

    def __init__(self, sb):
        self.sb = sb

    # selectors
    breadcrumb = '.breadcrumb-area'


    # helper methods for about us page
    def open(self):
        self.sb.open(ABOUT_US_PAGE_URL)