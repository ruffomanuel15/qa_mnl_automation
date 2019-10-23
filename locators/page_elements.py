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

<<<<<<< HEAD

class ClothingShopSelectors(object):
    IMAGE = (By.XPATH, "//ul[@id='homefeatured']//img")
    LABEL = (By.XPATH, "//ul[@id='homefeatured']//a[@class='product-name']")
    PRICE = (By.XPATH, "//ul[@id='homefeatured']//div[1]/span[@class='price product-price']")
=======
class ClothingShopSelectors(object):
    VAR = () #placeholder
>>>>>>> master
