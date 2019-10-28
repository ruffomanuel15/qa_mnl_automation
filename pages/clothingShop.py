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

class AddToCart(BasePage):
    def is_title_matches(self):
        return "Dresses - My Store" in self.driver.title

    def add_to_cart(self):
        # Go to Dress tab
        dressesTab = self.driver.find_element(*AddToCartSelectors.DRESSES_TAB)
        dressesTab.click()

        # Go to evening Dress tab
        eveningDress = self.driver.find_element(*AddToCartSelectors.EVENING_DRESSES)
        eveningDress.click()

        # Hover to Printed Dress Item
        printedDress = self.driver.find_element(*AddToCartSelectors.PRINTED_DRESS)
        hover = ActionChains(self.driver).move_to_element(printedDress)
        hover.perform()

        # Click 'More' CTA
        more = self.driver.find_element(*AddToCartSelectors.MORE_CTA)
        assert more.get_attribute("title") == "View"
        more.click()

        # Assert 'Prod Info" is present
        prodinfo = self.driver.find_element(*AddToCartSelectors.PROD_INFO)
        assert prodinfo.is_displayed(), 'Product info is not found'

        # Enter Quantity
        quantity = self.driver.find_element(*AddToCartSelectors.PROD_QUANTITY)
        quantity.clear()
        quantity.send_keys("8")

        # Select size 'M'
        sizeSelect = self.driver.find_element(*AddToCartSelectors.PROD_SIZE)
        sel = Select(sizeSelect)
        sel.select_by_visible_text("M")

        # Select color 'Pink'
        color = self.driver.find_element(*AddToCartSelectors.PROD_COLOR)
        color.click()

        # Click 'Add to cart' CTA
        addToCartBtn = self.driver.find_element(*AddToCartSelectors.ADDTOCART_CTA)
        addToCartBtn.click()
        time.sleep(5)


    def screenshot(self):
        Commands.take_screenshot(self.driver, test="assertion_tests")