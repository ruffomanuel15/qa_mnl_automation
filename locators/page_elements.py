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
    POPULARSECTION = (By.XPATH, "//*[@id='homefeatured']//a")
    POPULARLABEL = (By.XPATH, "//*[@id='homefeatured']//a[@class ='product-name']")
    POPULARPRICE = (By.XPATH, "//*[@id='homefeatured']//div[1]/span[@class='price product-price']")
    POPULARIMAGE = (By.XPATH, "//*[@id='homefeatured']//img")
    BESTSELLERSECTION = (By.XPATH, "//*[@id='blockbestsellers']//a")
    BESTLABEL = (By.XPATH, "//*[@id='blockbestsellers']//a[@class ='product-name']")
    BESTPRICE = (By.XPATH, "//*[@id='blockbestsellers']//div[1]/span[@class='price product-price']")
    BESTIMAGE = (By.XPATH, "//*[@id='blockbestsellers']//img")
    BEST_CTA = (By.XPATH, "//*[@id='home-page-tabs']/li[2]/a")
    POPULAR_CTA = (By.XPATH, "//*[@id='home-page-tabs']/li[1]/a")