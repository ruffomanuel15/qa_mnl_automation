from locators.page_elements import *
from utils import environment as env
from extensions.commands import *




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ClothingShop(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

<<<<<<< HEAD
    def assertion_tests(self):
        images = self.driver.find_elements(*ClothingShopSelectors.IMAGE)
        for img in images:
            src = img.get_attribute('src')
            print(src)
            assert src is not None, "Image Source is not present"
        productName = self.driver.find_elements(*ClothingShopSelectors.LABEL)
        for product in productName:
            label = product.text
            print(label)
            assert label is not None, "Product Label is not present"
        productPrice = self.driver.find_elements(*ClothingShopSelectors.PRICE)
        for pprice in productPrice:
            price = pprice.text
            print(price)
            assert price is not None, "Product Price is not present"






        # TODO
        # Objective:
        # 1. Configure environment.py to access the test url.
        # 2. Identify and store elements in the page_elements file.
        # 3. Make assertions to validate that each shop item in the section has an image (image source is not empty),
        # label and price.
=======
    def add_to_cart(self):
        var = () #placeholder
>>>>>>> master
