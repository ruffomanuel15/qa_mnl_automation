from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

def add_to_cart(self):
    #MAIN PAGE
    top_menu = self.driver.find_element(*AddToCartSelectors.TOP_MENU)
    dresses = top_menu.find_element(*AddToCartSelectors.DRESSES)

    assert top_menu.is_displayed(), "Top Menu is Missing"

    #Click Dresses Tab
    dresses.click()

    #DRESSES PAGE
    product_list = self.driver.find_element(*ClothingShopSelectors.PRODUCT_LIST)
    printed_dresses = product_list.find_element(*AddToCartSelectors.PRINTED_DRESS)

    assert printed_dresses.is_displayed(), "Printed Dresses is Missing"
    #Scroll to the specific Printed Dresses and Hover
    printed_dresses.location_once_scrolled_into_view

    #To make sure that the element will be hovered
    time.sleep(3)

    hover = ActionChains(self.driver).move_to_element(printed_dresses)
    hover.perform()

    #Click More
    more_button = printed_dresses.find_element(*AddToCartSelectors.MORE_BUTTON)
    more_button.click()

    #SPECIFIC ITEM PAGE
    #Size, Color, and Add to Cart
    size_dropdown = self.driver.find_element(*AddToCartSelectors.SIZE_DROPDOWN)
    size = "M"
    color_picker = self.driver.find_element(*AddToCartSelectors.COLOR_PICKER)
    color = "Pink"
    add_to_cart = self.driver.find_element(*AddToCartSelectors.ADD_TO_CART)


    #Set Size
    size_dropdown.find_element(By.XPATH, './option[@title="'+size+'"]').click()

    #Set Color
    color_picker.find_element(By.XPATH, './li/a[@title="' + color + '"]').click()

    #Click Add to Cart
    add_to_cart.click()

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