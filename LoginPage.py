from BasePage import Page
from Locators import *



class LoginPage(Page):
    def __init__(self, driver):
        self.locator = AuthenticationPage
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email_create(self, user):
        self.find_element(*self.locator.email_create).send_keys(user)

    def click_submit_create(self):
        self.find_element(*self.locator.submit_create).click()

    def login(self, user):
        self.enter_email_create(user)
        self.click_submit_create()