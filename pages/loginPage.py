from locators.page_elements import *
from utils import environment as env


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def is_title_matches(self):
        return "Log in to Sell-In" in self.driver.title

    """Login creds for use in checkout flow"""
    def login_as_standard_user(self):
        username = self.driver.find_element(*LoginPageLocators.USN_INPUT)
        password = self.driver.find_element(*LoginPageLocators.PWD_INPUT)
        submit_login = self.driver.find_element(*LoginPageLocators.LOGIN_CTA)

        username.send_keys(env.user)
        password.send_keys(env.pwd)
        submit_login.click()