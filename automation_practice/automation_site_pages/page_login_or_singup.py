from seleniumbase import BaseCase
from config.defaults import BASE_URL
from config.defaults import EMAIL1
from config.defaults import password


class PageLoginOrSignup:

    def __init__(self, sb : BaseCase):
        self.sb = sb

        # selectors
        self.login = ".shop-menu a[href='/login']"
        self.email_selector = "input[name='email']"
        self.password_selector = "input[name='password']"
        self.login_button = "button[data-qa='login-button']"
        self.logged_in_user = "li:nth-child(10) a:nth-child(1)"
        self.logout_button = ".shop-menu a[href='/logout']"
        self.name = "input[name='name']"
        self.signup_email_selector = "input[data-qa='signup-email']"
        self.signup_submit_button = "button[data-qa='signup-button']"
        self.title = "#id_gender2"
        self.signup_name = "#name"
        self.signup_email = "input[data-qa='signup-email']"
        self.signup_password = "#password"
        self.signup_day = "select[data-qa='days']"
        self.signup_month = "#months"
        self.signup_year = "#years"
        self.signup_checkbox_newsletter = "#newsletter"
        self.signup_special_offer_checkbox = "#optin"
        self.signup_first_name = "#first_name"
        self.signup_last_name = "#last_name"
        self.signup_company = "#company"
        self.signup_address = "#address1"
        self.signup_address2 = "#address2"
        self.signup_country = "#country"
        self.signup_state = "#state"
        self.signup_city = "#city"
        self.signup_zipcode = "#zipcode"
        self.signup_mobile_number = "#mobile_number"
        self.create_account = "button[data-qa='create-account']"

    # Helper methods
    def open(self):
        self.sb.open(BASE_URL)

    def login_method(self, email, password):
        self.sb.type(self.email_selector, email )
        self.sb.type(self.password_selector, password)

    # Verify that 'Logged in as username' is visible
    def verify_logged_in_username_is_correct(self):
        text = self.sb.get_text(self.logged_in_user)
        self.sb.assert_in('python', text)
        self.sb.assert_element_visible(self.logged_in_user)

    def enter_signup_details(self):
        self.sb.click(self.title)
        self.sb.type(self.signup_name, "world")
        #self.sb.type(self.signup_email, EMAIL1)
        self.sb.type(self.signup_password, password)

        # date of birth
        self.sb.select_option_by_text(self.signup_day, "26")
        self.sb.select_option_by_index(self.signup_month, "4")
        self.sb.select_option_by_index(self.signup_year, "4" )

    def enter_signup_address_information(self):
        self.sb.type(self.signup_first_name, "javapo")
        self.sb.type(self.signup_last_name, "worldno")
        self.sb.type(self.signup_company, "gunaworld")
        self.sb.type(self.signup_address, "chennai1")
        self.sb.type(self.signup_address2, "airport1")
        self.sb.select_option_by_value(self.signup_country,"India")
        self.sb.type(self.signup_state, "andhra")
        self.sb.type(self.signup_city, "kandriga")
        self.sb.type(self.signup_zipcode, "839839")
        self.sb.type(self.signup_mobile_number, "7362389825")


