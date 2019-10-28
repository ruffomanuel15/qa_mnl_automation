""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USN_INPUT = (By.XPATH, 'sample_xpath')
    PWD_INPUT = (By.XPATH, 'sample_xpath')
    LOGIN_CTA = (By.XPATH, 'sample_xpath')


class LandingPageLocators(object):
    SEARCH_CTA = (By.XPATH, 'sample_xpath')


class Search(object):
    SEARCH_FIELD = (By.XPATH, '//input[@title="Search"]')
    SEARCH_CTA = (By.XPATH, '(//input[@value="Google Search"])[2]')


class LetsKodeitSelectors(object):
    TABLE = (By.CLASS_NAME, 'table-display')
    TR = (By.TAG_NAME, "tr")
    TH = (By.TAG_NAME, "th")
    TD = (By.TAG_NAME, "td")

class ClothingShopSelectors(object):
    POPULARSECTION = (By.XPATH, "//ul[@id='homefeatured']")
    POPULARLABEL = (By.XPATH, "//ul[@id='homefeatured']//a[@class ='product-name']")
    POPULARPRICE = (By.XPATH, "//ul[@id='homefeatured']//div[1]/span[@class='price product-price']")
    POPULARIMAGE = (By.XPATH, "//ul[@id='homefeatured']//img")


class AddToCartSelectors(object):
    DRESSES_TAB = (By.XPATH, "//div[@id='block_top_menu']/ul/li/a[@title='Dresses']")
    EVENING_DRESSES = (By.XPATH, "//div[@id='subcategories']//a[text()='Evening Dresses']")
    PRINTED_DRESS = (By.XPATH, "//div[@class='product-image-container']//a[@title='Printed Dress']")
    MORE_CTA = (By.XPATH, "//div[@id='center_column']/ul//div[@class='product-container']//a[@title='View']")
    PROD_INFO = (By.XPATH, "//div[@class='box-info-product']")
    PROD_QUANTITY = (By.XPATH, "//input[@id='quantity_wanted']")
    PROD_SIZE = (By.XPATH, "//select[@id='group_1']")
    PROD_COLOR = (By.XPATH, "//a[@id='color_24']")
    ADDTOCART_CTA = (By.XPATH, "//button[@class='exclusive']")

class PhpTravelsLocators(object):
    FT_LABEL = (By.XPATH,"//div/h2[text()='Featured Tours']")
    FT_SECTION =(By.XPATH, "//div[@class='container']//div[contains(@class, 'cols-2')]")
    FT_CARD = (By.XPATH, "//div[@class='container']//figure[starts-with(@class, 'featured-image')]")
    FT_CARD_CONTENT = (By.XPATH, "//div[@class='container']//figcaption[@class='content']")
    FT_PRICE = (By.XPATH, ".//div/div/span/span")
    FT_NAME = (By.XPATH, ".//h5[@class='mb-0 RTL']")
    FT_DURATION = (By.XPATH, ".//span[@class='item-expire']")
    FT_LOCATION = (By.XPATH, ".//p[@class='location go-text-right']")