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
    # BESTSELLERSECTION = (By.XPATH, "//ul[@id='blockbestsellers']//a")
    # BESTLABEL = (By.XPATH, "//ul[@id='blockbestsellers']//a[@class ='product-name']")
    # BESTPRICE = (By.XPATH, "//ul[@id='blockbestsellers']//div[1]/span[@class='price product-price']")
    # BESTIMAGE = (By.XPATH, "//ul[@id='blockbestsellers']//img")
    # BEST_CTA = (By.XPATH, "//ul[@id='home-page-tabs']/li[2]/a")
    # POPULAR_CTA = (By.XPATH, "//ul[@id='home-page-tabs']/li[1]/a")