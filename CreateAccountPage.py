from selenium.webdriver.support.select import Select
from BasePage import Page
from Locators import *



class CreateAccountPage(Page):
    def __init__(self, driver):
        self.locator = AccountCreatePage
        super(CreateAccountPage, self).__init__(driver)

    def enter_firstname(self, firstname):
        self.find_element(*self.locator.first_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.find_element(*self.locator.last_name).send_keys(lastname)

    def enter_passwd(self, passwd):
        self.find_element(*self.locator.passwd).send_keys(passwd)

    def enter_address1(self, address1):
        self.find_element(*self.locator.address1).send_keys(address1)

    def enter_city(self, city):
        self.find_element(*self.locator.city).send_keys(city)

    def enter_state(self, state):
        Select(self.find_element(*self.locator.state)).select_by_value(state)

    def enter_country(self, country):
        Select(self.find_element(*self.locator.country)).select_by_value(country)

    def enter_postcode(self, postcode):
        self.find_element(*self.locator.post_code).send_keys(postcode)

    def enter_homephone(self, homephone):
        self.find_element(*self.locator.home_phone).send_keys(homephone)

    def enter_mobilephone(self, mobilephone):
        self.find_element(*self.locator.mobile_phone).send_keys(mobilephone)

    def enter_addresstitle(self, addresstitle):
        self.find_element(*self.locator.address_title).send_keys(addresstitle)

    def click_submit_address(self):
        self.find_element(*self.locator.save_button).click()

    def create_account(self, firstname, lastname, passwd, address1, city, state, country, post_code, home_phone, mobile_phone, address_title):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_passwd(passwd)
        self.enter_address1(address1)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_country(country)
        self.enter_postcode(post_code)
        self.enter_homephone(home_phone)
        self.enter_mobilephone(mobile_phone)
        self.enter_addresstitle(address_title)
        self.click_submit_address()

