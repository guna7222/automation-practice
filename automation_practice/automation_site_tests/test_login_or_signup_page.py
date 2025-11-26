

from seleniumbase import BaseCase
from automation_site_pages.page_login_or_singup import PageLoginOrSignup
from config.defaults import LOGIN_URL
from config.defaults import email
from config.defaults import password
from parameterized import parameterized
from config.defaults import EMAIL1
from config.defaults import username
import pytest

class TestLoginOrSignupPage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp() # calls the setup of parent class
        self.object_login_or_singUp = PageLoginOrSignup(self)
        self.object_login_or_singUp.open()

    @parameterized.expand([
        (email,password),
        (EMAIL1, password)
         ])
    def test_logout_page(self, email, password1):
        #  Verify that home page is visible successfully
        self.assert_text_visible("Home")

        #Click on 'Signup / Login' button
        self.click(self.object_login_or_singUp.login)

        # Verify 'Login to your account' is visible
        self.assert_text_visible("Login to your account")

        # Enter correct email address and password
        self.object_login_or_singUp.login_method(email, password1)

        # Click 'login' button
        self.click(self.object_login_or_singUp.login_button)

        # Verify that 'Logged in as username' is visible
        self.object_login_or_singUp.verify_logged_in_username_is_correct()

        #Click 'Logout' button
        self.click(self.object_login_or_singUp.logout_button)

        # Verify that user is navigated to login page
        self.assert_url(LOGIN_URL)

    @pytest.mark.smoke
    @pytest.mark.register_user
    def test_register_user(self):
        #  Verify that home page is visible successfully
        self.assert_text_visible("Home")

        # Click on 'Signup / Login' button
        self.click(self.object_login_or_singUp.login)

        #  Verify 'New User Signup!' is visible
        self.assert_text_visible("New User Signup!")

        # Enter name and email address
        self.type(self.object_login_or_singUp.name, username)
        self.type(self.object_login_or_singUp.signup_email_selector, EMAIL1)
        self.sleep(10)
        # Click 'Signup' button
        self.click(self.object_login_or_singUp.signup_submit_button)

        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        #self.assert_text_visible("Enter Account Information")

        # . Fill details: Title, Name, Email, Password, Date of birth
        self.object_login_or_singUp.enter_signup_details()

        #  Select checkbox 'Sign up for our newsletter!'
        self.click(self.object_login_or_singUp.signup_checkbox_newsletter)

        #  Select checkbox 'Receive special offers from our partners!'
        self.click(self.object_login_or_singUp.signup_special_offer_checkbox)

        # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        self.object_login_or_singUp.enter_signup_address_information()

        # Click 'Create Account button'
        self.click(self.object_login_or_singUp.create_account)