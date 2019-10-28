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
    PRODUCT_LIST = (By.CLASS_NAME, "product_list")
    PRODUCT = (By.CLASS_NAME, "product-container")
    PRODUCT_TOP = (By.CLASS_NAME, "left-block")
    PRODUCT_BOTTOM = (By.CLASS_NAME, "right-block")
    NAME = (By.CLASS_NAME, "product-name")
    PRICE = (By.TAG_NAME, "span")
    IMAGE = (By.TAG_NAME, "img")


    VAR = () #placeholder