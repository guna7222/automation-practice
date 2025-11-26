import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seleniumbase import BaseCase
from config.defaults import DEMO_PAGE_URL

class TestDemoPage(BaseCase):

# testing input slider
    def test_input_slider_functionality(self):
        self.open(DEMO_PAGE_URL)
        # before state
        self.assert_attribute('#progressBar', 'value', '50')

        # action: move the slider to 80
        self.set_value('#mySlider', '80')

        self.assert_attribute('#progressBar', 'value', '80' )\

    # working with Iframe
    def test_iframe_interaction(self):
        self.open(DEMO_PAGE_URL)
        # switch to iframe
        self.switch_to_frame('#myFrame2')
        self.assert_text('iFrame Text', 'h4')
        self.switch_to_default_content()
        self.assert_text_visible("SeleniumBase")