from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LetsKodeItPage(BasePage):

    def is_title_matches(self):
        return "Practice | Let's Kode It" in self.driver.title

    def assertion_tests(self):
        table = self.driver.find_element(*LetsKodeitSelectors.TABLE)
        assert table.is_displayed(), 'Table is missing'

        # TODO assert the remaining elements in the tabl
