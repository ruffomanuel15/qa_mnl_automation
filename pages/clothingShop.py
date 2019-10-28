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

    def assertion_tests(self):
        #Get the Grid
        product_list = self.driver.find_element(*ClothingShopSelectors.PRODUCT_LIST)

        #Verify if Grid Exists
        assert product_list.is_displayed(), 'Grid is Missing'


        #Get each Product Block
        products = product_list.find_elements(*ClothingShopSelectors.PRODUCT)


        for product in products:
            #get the Image's block
            product_top = product.find_element(*ClothingShopSelectors.PRODUCT_TOP)

            #get the Name/Price's block
            product_bottom = product.find_element(*ClothingShopSelectors.PRODUCT_BOTTOM)

            #Get Name, Image Source, and Price
            name = product_bottom.find_element(*ClothingShopSelectors.NAME)
            image_src = product_top.find_element(*ClothingShopSelectors.IMAGE).get_attribute("src")
            price = product_bottom.find_element(*ClothingShopSelectors.PRICE)

            #Print Values
            print(name.text)
            print(image_src)
            print(price.text)

            #Assert if each item has a value
            assert name.text is not None, 'Name is Empty'
            assert image_src is not None, 'Image SRC is Empty'
            assert price.text is not None, 'Price is Empty'