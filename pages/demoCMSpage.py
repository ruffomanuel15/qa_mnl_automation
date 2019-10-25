from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class OpenSource(BasePage):
    def login_to_cms(self):
        #TODO
        # log in to CMS
        pass