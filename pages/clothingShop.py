from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.webdriver import ActionChains




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ClothingShop(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

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
        # label and price

    def add_to_cart(self):
        # Clicking Dresses tab
        dressesLink = self.driver.find_element(*AddToCartSelectors.DRESSESLINK)
        dressesLink.click()

        # Hovering on the Printed Dress Element
        summerDress = self.driver.find_element(*AddToCartSelectors.SUMMERDRESS)
        hover = ActionChains(self.driver).move_to_element(summerDress)
        hover.perform()
        time.sleep(2)

        # Clicking More button
        more = self.driver.find_element(*AddToCartSelectors.MORE)
        more.click()
        time.sleep(2)

        # Input Quantity
        quantity = self.driver.find_element(*AddToCartSelectors.QUANTITY)
        quantity.clear()
        quantity.send_keys("8")
        time.sleep(2)

        # Select M size
        sizeSelect = self.driver.find_element(*AddToCartSelectors.SIZESELECTION)
        sel = Select(sizeSelect)
        sel.select_by_visible_text("M")
        time.sleep(2)

        # Select Pink color
        color = self.driver.find_element(*AddToCartSelectors.COLORSELECTION)
        color.click()
        time.sleep(3)

        # Clicking Add to Cart button
        addToCartBtn = self.driver.find_element(*AddToCartSelectors.ADDTOCARDTBTN)
        addToCartBtn.click()
        time.sleep(5)

        # Take screenshot
        Commands.take_screenshot(self.driver, test="add_to_cart_test")




