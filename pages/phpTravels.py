from locators.page_elements import *
from extensions.commands import *
from datetime import datetime as DateTime, timedelta as TimeDelta


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class PhpTravels(BasePage):
    def is_title_matches(self):
        return "PHPTRAVELS | Travel Technology Partner" in self.driver.title

    def go_to_featured_tours(self):
        featuredtours = self.driver.find_element(*PhpTravelsLocators.FT_LABEL)
        self.driver.execute_script("arguments[0].scrollIntoView();", featuredtours)
        assert featuredtours is not None, "Tours not found"

    def featured_tours_info(self):
        higher = []
        lower = []

        # loop
        container = self.driver.find_elements(*PhpTravelsLocators.FT_CARD_CONTENT)
        for info in container:
            ftprice = info.find_element(*PhpTravelsLocators.FT_PRICE)
            ftname = info.find_element(*PhpTravelsLocators.FT_NAME)
            ftduration = info.find_element(*PhpTravelsLocators.FT_DURATION)
            ftlocation = info.find_element(*PhpTravelsLocators.FT_LOCATION)
            tourprice = ftprice.text[1::]

            # append prices
            if int(tourprice) > 100:
                higher.append(ftname.text)
                higher.append(ftduration.text)
                higher.append(ftlocation.text)

            elif int(tourprice) < 100:
                lower.append(ftname.text)
                lower.append(ftduration.text)
                lower.append(ftlocation.text)

        print("\n")
        print("The following are the tours that are higher than $100: " + str(higher) + "\n"
              + "\n" + "The following are the tours that are lower than $100: " + str(lower))

    def screenshot(self):
        Commands.take_screenshot(self.driver, test="featured_tours_info")


class PhpTravelSearch(BasePage):
    def is_title_matches(self):
        return "PHPTRAVELS | Travel Technology Partner" in self.driver.title

    def hotels_tab(self):
        # Go to Hotels tab
        hotelsTab = self.driver.find_element(*PhpTravelPackageLocators.TP_HOTELS_TAB)
        hotelsTab.click()

    def search_travel_package(self):
        # Search
        self.driver.find_element(*PhpTravelPackageLocators.TP_COOKIE_BTN).click()
        self.driver.find_element(*PhpTravelPackageLocators.TP_DESTINATION_FIELD).send_keys("Barce")
        self.driver.find_element(*PhpTravelPackageLocators.TP_DESTINATION_SELECT).click()
        time.sleep(1)
        self.driver.find_element(*PhpTravelPackageLocators.TP_CHECKIN_FIELD).click()
        self.driver.find_element(*PhpTravelPackageLocators.TP_CALENDAR_PICKER_IN).click()
        time.sleep(1)
        self.driver.find_element(*PhpTravelPackageLocators.TP_CHECKOUT_FIELD).click()
        time.sleep(1)
        self.driver.find_element(*PhpTravelPackageLocators.TP_CALENDAR_NEXT_BTN).click()
        self.driver.find_element(*PhpTravelPackageLocators.TP_CALENDAR_PICKER_OUT).click()
        time.sleep(1)
        self.driver.find_element(*PhpTravelPackageLocators.TP_GROUP_INCREMENT_BTN).click()
        self.driver.find_element(*PhpTravelPackageLocators.TP_SEARCH_BTN).click()

    def screenshot(self):
        Commands.take_screenshot(self.driver, test="search_travel_package")
