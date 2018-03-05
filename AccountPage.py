from BasePage import Page
from Locators import *



class AccountPage(Page):
    def __init__(self, driver):
        self.locator = AccountPageLocators
        super(AccountPage, self).__init__(driver)  # Python2 version

    def click_submit_personal_information(self):
        self.find_element(*self.locator.my_personal_information).click()

    def click_submit_personal_information(self):
        self.find_element(*self.locator.my_personal_information).click()

    def click_submit_my_addresses(self):
        self.find_element(*self.locator.my_addresses).click()

    def click_submit_my_personal_information_back_button(self):
        self.find_element(*self.locator.my_personal_information_back_button).click()

    def get_values_firstname(self):
        element = self.find_element(*self.locator.first_name)
        return element.get_attribute('value')

    def get_values_lastname(self):
        element = self.find_element(*self.locator.last_name)
        return element.get_attribute('value')

    def get_values_my_addresses(self):
        element = self.find_element(*self.locator.my_addresses_values)
        return element.text
