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

    def assertion_tests(self):
        #pop = self.driver.find_element(*ClothingShopSelectors.POPULAR_CTA)
        shopSection = self.driver.find_element(*ClothingShopSelectors.POPULARSECTION)
        images = shopSection.find_elements(*ClothingShopSelectors.POPULARIMAGE)
        for img in images:
            src = img.get_attribute('src')
            print(src)
            assert src is not None, "Popular image source not found"
        productName = shopSection.find_elements(*ClothingShopSelectors.POPULARLABEL)
        for product in productName:
            label = product.text
            print(label)
            assert label is not None, "Popular product label not found"
        productPrice = shopSection.find_elements(*ClothingShopSelectors.POPULARPRICE)
        for price in productPrice:
            price = price.text
            print(price)
            assert price is not None, "Popular product price not found"

        # best = self.driver.find_element(*ClothingShopSelectors.BEST_CTA)
        # best.click()
        # shopSection = self.driver.find_element(*ClothingShopSelectors.BESTSELLERSECTION)
        # images = shopSection.find_elements(*ClothingShopSelectors.BESTIMAGE)
        # for img in images:
        #     src = img.get_attribute('src')
        #     print(src)
        #     assert src is not None, "Best seller image source not found"
        # productName = shopSection.find_elements(*ClothingShopSelectors.BESTLABEL)
        # for product in productName:
        #     label = product.text
        #     print(label)
        #     assert label is not None, "Best seller product label not found"
        # productPrice = shopSection.find_elements(*ClothingShopSelectors.BESTPRICE)
        # for price in productPrice:
        #     price = price.text
        #     print(price)
        #     assert price is not None, "Best seller product price not found"

        # TODO
        # Objective:
        # 1. Configure environment.py to access the test url.
        # 2. Identify and store elements in the page_elements file.
        # 3. Make assertions to validate that each shop item in the section has an image (image source is not empty),
        # label and price.
