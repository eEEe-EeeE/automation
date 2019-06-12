from selenium.webdriver.common.by import By
from .base_page import BasePage


class Login(BasePage):

    # Initialization

    def __init__(self, selenium_driver, base_url='http://192.168.1.23/#/'):
        super().__init__(selenium_driver, base_url)

    # Xpath

    __login_username_loc = (By.ID, "username")
    __login_password_loc = (By.ID, "password")
    __login_button_loc = (By.TAG_NAME, "button")

    # Locator

    def __login_username(self, username):
        self.find_element(*self.__login_username_loc).send_keys(username)

    def __login_password(self, password):
        self.find_element(*self.__login_password_loc).send_keys(password)

    def __login_button(self):
        self.find_element(*self.__login_button_loc).click()

    # Action

    def user_login(self, username, password):
        self.open()
        self.__login_username(username)
        self.__login_password(password)
        self.__login_button()

    # Assert

    # username_error_hint_loc = (By.XPATH, '')
    # password_error_hint_loc = (By.XPATH, '')
    user_login_success_loc = (By.XPATH, '//div/div[1]/div')

    # def username_error_hint(self):
    #     return self.find_element(*self.username_error_hint_loc).text
    #
    # def password_error_hint(self):
    #     return self.find_element(*self.password_error_hint_loc).text

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
