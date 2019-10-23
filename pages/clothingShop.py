from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ClothingShop(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

    def add_to_cart(self):
        var = () #placeholder