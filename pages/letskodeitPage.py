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

        #Julian Challenge 3

        #Get Rows#
        rows = table.find_elements(*LetsKodeitSelectors.TR)

        #Get Headers


        #Check Items Per Row
        for row in rows:
            headers = row.find_elements(*LetsKodeitSelectors.TH)
            data = row.find_elements(*LetsKodeitSelectors.TD)


            #Print Headers and Rows
            for header in headers:
                print(header.text)

            for item in data:
                print(item.text)

            #Assertion Per Row Checked
            assert headers is not None, 'Table Header element is not displayed'
            assert data is not None, 'Table Header element is not displayed'


