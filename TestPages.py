import unittest
from selenium import webdriver


from LoginPage import LoginPage
from CreateAccountPage import CreateAccountPage
from AccountPage import AccountPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    def test_sign_in_button(self):
        print("\n" + str("teste 1"))
        login_page = LoginPage(self.driver)
        login_page.login("josedasilva20@gmail.com")
        createAccount_page = CreateAccountPage(self.driver)
        self.driver.implicitly_wait(10)
        createAccount_page.create_account("teste", "teste", "frlc_3112", "rua do teste", "florida", "5", "21", "00000", "9858858", "98585588", "teste address")
        account_page = AccountPage(self.driver)

        account_page.click_submit_personal_information()
        self.driver.implicitly_wait(5)
        value_firstname = account_page.get_values_firstname()
        value_lastname = account_page.get_values_lastname()

        account_page.click_submit_my_personal_information_back_button()
        self.driver.implicitly_wait(5)

        account_page.click_submit_my_addresses()
        self.driver.implicitly_wait(5)
        value_addresses = account_page.get_values_my_addresses()


        self.assertEqual("teste", value_firstname)
        self.assertEqual("teste", value_lastname)
        self.assertEqual("rua do teste", value_addresses)


    def tearDown(self):
       self.driver.close()


if __name__ == '__main__':
    unittest.main()
