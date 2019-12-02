from locators.page_elements import *
from extensions.commands import *

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
        print("The following are the tours that are higher than $100: " + str(higher)+"\n"
              +"\n" + "The following are the tours that are lower than $100: " + str(lower))


    def screenshot(self):
        Commands.take_screenshot(self.driver, test="featured_tours_info")