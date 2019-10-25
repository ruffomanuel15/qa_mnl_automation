from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver import ActionChains




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class PHPTravelsPage(BasePage):
    def is_title_matches(self):
        return "PHPTRAVELS | Travel Technology Partner" in self.driver.title

    def featured_tours_details(self):
        Above100 = []
        Less100 = []

        container = self.driver.find_elements(*PHPTravelsLocators.CONTAINER)
        for con in container:
            tourprice = con.find_element(*PHPTravelsLocators.PRICE)
            tourname = con.find_element(*PHPTravelsLocators.TOURNAME)
            duration = con.find_element(*PHPTravelsLocators.DURATION)
            location = con.find_element(*PHPTravelsLocators.LOCATION)
            price = tourprice.text[1::]

            if int(price) > 100:
                Above100.append(tourname.text)
                Above100.append(duration.text)
                Above100.append(location.text)

            elif int(price) < 100:
                Less100.append(tourname.text)
                Less100.append(duration.text)
                Less100.append(location.text)

        print("\n" + "*"*50)
        print("Tours that are above $100: " + str(Above100))
        print("\n" + "*"*50)
        print("Tours that are less $100: " + str(Less100))













