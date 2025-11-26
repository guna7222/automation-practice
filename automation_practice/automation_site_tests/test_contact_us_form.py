

from seleniumbase import BaseCase

from automation_practice.automation_site_pages.page_contact_us_form import PageContactUsForm


class TestContactUsForm(BaseCase):

    def test_contact_us_form(self):
        contact_us_page = PageContactUsForm(self)
        contact_us_page.open()
        #  Verify that home page is visible successfully
        self.assert_text_visible("Home")
        # Click on 'Contact Us' button
        self.click(contact_us_page.contact_us_button)
        # Verify 'GET IN TOUCH' is visible
        self.assert_text_visible("GET IN TOUCH")
        #  Enter name, email, subject and message
        contact_us_page.fill_the_form()
        # Upload file
        contact_us_page.upload_file()

        # Disable the alert popup (so it doesn't block)
        self.execute_script("window.alert = function(msg){ return true; };")

        # Click the submit button
        self.click(contact_us_page.submit_button)

        # # Manually trigger the submit since alert was suppressed
        # self.execute_script("document.querySelector('form[action=\"/contact_us\"]')?.submit();")
        #
        # # Wait for success message to appear
        # self.assert_text_visible(
        #     "Success! Your details have been submitted successfully.",
        #     timeout=15,
        # )
        #
        # # Click 'Home' button and verify navigation
        # self.click(contact_us_page.about_us_home)
        # self.assert_text_visible("Home")