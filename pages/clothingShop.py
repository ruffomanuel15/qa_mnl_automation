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

    def assertion_tests(self, product_tab):
        # Julian Challenge 4

        # Selecting the Tab (for example, there are 2 tabs on the site)
        selected_tab = self.driver.find_element(By.XPATH, './/*[contains(text(),"' + product_tab + '")]')
        selected_tab.click()

        # Check if the grid is displayed
        product_grid = self.driver.find_element(*ClothingShopSelectors.PRODUCT_GRID)
        assert product_grid.is_displayed(), 'Grid is Missing'

        # Get each product in the grid
        products = product_grid.find_elements(*ClothingShopSelectors.PRODUCT_ITEM)

        # Print Tab Title
        print("\n" + product_tab)

        # Checking each product
        for product in products:
            # Get the  Image Block (top part of the product) and the Detail lock (bottom)
            product_image = product.find_element(*ClothingShopSelectors.PRODUCT_TOP)
            product_detail = product.find_element(*ClothingShopSelectors.PRODUCT_BOT)

            # Get the Image, Name, and Price of each product
            product_imagesrc = product_image.find_element(*ClothingShopSelectors.IMAGE_SRC).get_attribute('src')
            product_name = product_detail.find_element(*ClothingShopSelectors.PRODUCT_NAME)
            product_price = product_detail.find_element(*ClothingShopSelectors.PRODUCT_PRICE)

            # Check if one of the elements is not displayed
            assert product_imagesrc is not None, 'Image SRC is empty'
            assert product_price.text is not None, 'Product Price is empty'
            assert product_name is not None, 'Product Name is empty'

            # Print every product detail
            print("\nName: " + product_name.text)
            print("Price: " + product_price.text)
            print("Image SRC: " + product_imagesrc)

    def add_to_cart(self):
        var = () #placeholder