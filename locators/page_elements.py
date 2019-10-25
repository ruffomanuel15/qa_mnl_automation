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
    IMAGE = (By.XPATH, "//ul[@id='homefeatured']//img")
    LABEL = (By.XPATH, "//ul[@id='homefeatured']//a[@class='product-name']")
    PRICE = (By.XPATH, "//ul[@id='homefeatured']//div[1]/span[@class='price product-price']")


class AddToCartSelectors(object):
    DRESSESLINK = (By.XPATH, "//div[@id='block_top_menu']/ul/li/a[@title='Dresses']")
    SUMMERDRESS = (By.XPATH, "//ul[@class='product_list grid row']/li[2]")
    MORE = (By.XPATH, "//div[@id='center_column']/ul/li[2]/div[@class='product-container']//a[@title='View']")
    QUANTITY = (By.XPATH, "//input[@id='quantity_wanted']")
    SIZESELECTION = (By.XPATH, "//select[@id='group_1']")
    COLORSELECTION = (By.XPATH, "//a[@id='color_24']")
    ADDTOCARDTBTN = (By.XPATH, "//button[@class='exclusive']")

class PHPTravelsLocators(object):
    CONTAINER = (By.XPATH, "//figure[@class='featured-image-grid-item with-highlight']")
    PRICE = (By.XPATH, ".//span[@class='item-highlight text-secondary']/span")
    TOURNAME = (By.XPATH, ".//h5")
    DURATION = (By.XPATH, ".//span[@class='item-expire']")
    LOCATION = (By.XPATH, ".//p[@class='location go-text-right']")


