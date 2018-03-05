from selenium.webdriver.common.by import By

class AuthenticationPage(object):
  email_create = (By.ID, 'email_create')
  submit_create = (By.ID, 'SubmitCreate')


class AccountCreatePage(object):
  first_name = (By.XPATH, '//*[@id="customer_firstname"]')
  last_name = (By.ID, 'customer_lastname')
  passwd = (By.ID, 'passwd')
  address1 = (By.ID, 'address1')
  city = (By.ID, 'city')
  state = (By.ID, 'id_state')
  country = (By.ID, 'id_country')
  post_code = (By.ID, 'postcode')
  home_phone = (By.ID, 'phone')
  mobile_phone = (By.ID, 'phone_mobile')
  address_title = (By.ID, "alias")
  save_button = (By.ID, 'submitAccount')



class AccountPageLocators(object):
    my_personal_information = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[1]/ul/li[4]/a')
    first_name = (By.ID, 'firstname')
    last_name = (By.ID, 'lastname')
    my_personal_information_back_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/ul/li[1]/a')
    my_addresses = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[1]/ul/li[3]/a')
    my_addresses_values = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div[1]/div/div/ul/li[4]/span[1]')


