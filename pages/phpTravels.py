from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By
import datetime


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class PHPTravels(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

    def get_list(self):
        featured_tours = self.driver.find_element(*PHPTravelsSelectors.FEATURED_TOURS)
        assert featured_tours.is_displayed(), "No Featured Tours"
        self.driver.execute_script("arguments[0].scrollIntoView();", featured_tours)
        time.sleep(3)

        #Get All Items
        tour_items = featured_tours.find_elements(*PHPTravelsSelectors.TOUR_ITEMS)

        #Create an Empty Dictionary - used dictionary for a cleaner/more defined print later
        below_100 = {}
        above_100 = {}

        #Check each Tour Item
        for tour_item in tour_items:

            #Get the price, duration and location
            item_caption = tour_item.find_element(*PHPTravelsSelectors.ITEM_CAPTION)
            price = item_caption.find_element(*PHPTravelsSelectors.PRICE)
            #Strip the dollar sign and convert to int
            price = int((price.text).strip("$"))
            duration = item_caption.find_element(*PHPTravelsSelectors.DURATION)
            location = item_caption.find_element(*PHPTravelsSelectors.LOCATION)
            title = item_caption.find_element(*PHPTravelsSelectors.TITLE)

            #check if price has value
            assert price is not None, "Price is Missing"

            #Separate which are below and above $100
            #Dictionary Structure: {Tour Name:{Price,Duration,Location}}
            if (price < 100 ):

                below_100[title.text] = {}
                below_100[title.text]["Price"] = price
                below_100[title.text]["Duration"] = duration.text
                below_100[title.text]["Location"] = location.text

            elif (price > 100):
                above_100[title.text] = {}
                above_100[title.text]["Price"] = price
                above_100[title.text]["Duration"] = duration.text
                above_100[title.text]["Location"] = location.text

        #Print the items below 100
        print("\nFeatured Tours below $100:")
        for key, value in below_100.items():
            print(key, ":", value)

        #Print the items above 100
        print("\nFeatured Tours above $100:")
        for key, value in above_100.items():
            print(key, ":", value)

    def click_2nd_car(self):
        featured_cars = self.driver.find_element(*PHPTravelsSelectors.FEATURED_CARS)
        car_items = featured_cars.find_elements(*PHPTravelsSelectors.CAR_ITEMS)

        #scroll into view of the featured cars
        self.driver.execute_script("arguments[0].scrollIntoView();", featured_cars)

        #click 2nd item
        car_items[1].click()

        #just to check if it goes to the page
        time.sleep(3)

class TravelPackage(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

    def dest(self):

        #Search in the searchbar using "Barce"
        destination = self.driver.find_element(*PHPTravelsSelectors.DESTINATION)
        destination.send_keys("Barce")

        #Click the completed "Barcelona, Spain"
        completion = self.driver.find_element(*PHPTravelsSelectors.COMPLETION)
        completion.click()

        #Get current date
        currentdate = datetime.date.today()

        #Input the current date in Check In
        checkin = self.driver.find_element(*PHPTravelsSelectors.CHECKIN)
        checkin.click()
        checkin.clear()
        checkin.send_keys(currentdate.strftime("%d/%m/%Y")) #Format is set to DD/MM/YYYY

        #Add 5 days to the current date
        currentdate_5 = currentdate + datetime.timedelta(days=5)

        #Input the 5 days later in Check Out
        checkout = self.driver.find_element(*PHPTravelsSelectors.CHECKOUT)
        checkout.click()
        checkout.clear()
        checkout.send_keys(currentdate_5.strftime("%d/%m/%Y")) #Format is set to DD/MM/YYYY

        #Add 1 child
        add_children = self.driver.find_element(*PHPTravelsSelectors.ADD_CHILDREN)
        add_children.click()

        #Click Search button
        search_btn = self.driver.find_element(*PHPTravelsSelectors.SEARCH_BTN)
        search_btn.click()

    def take_screenshot(self):
        time.sleep(5)
        Commands.take_screenshot(self.driver, test="My Purchase")