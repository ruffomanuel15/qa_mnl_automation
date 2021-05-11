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

        # Julian - Challenge 3

        # Scroll to the table
        self.driver.execute_script("arguments[0].scrollIntoView();", table)

        # Check all the rows
        tRows = table.find_elements(*LetsKodeitSelectors.TR)

        for row in tRows:
            tHeaders = row.find_elements(*LetsKodeitSelectors.TH)
            tData = row.find_elements(*LetsKodeitSelectors.TD)

            # Print Table Headers and Data if not empty, assert if empty
            for header in tHeaders:
                assert header is not None, 'Table Header element is not displayed'
                print(header.text)

            for data in tData:
                assert data is not None, 'Table Data element is not displayed'
                print(data.text)
