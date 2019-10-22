from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ClothingShop(BasePage):

    def assertion_tests(self):
        ShopSection = ()

        # TODO
        # Objective:
        # 1. Configure environment.py to access the test url.
        # 2. Identify and store elements in the page_elements file.
        # 3. Make assertions to validate that each shop item in the section has an image (image source is not empty),
        # label and price.