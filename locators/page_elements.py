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

class PhpTravelPackageLocators(object):
    TP_HOTELS_TAB = (By.XPATH, "//div[@class='container']//a[@href='#hotels']")
    TP_DESTINATION_FIELD = (By.XPATH, "//input[@id='s2id_autogen2']")
    TP_DESTINATION_SELECT = (By.XPATH, "//ul[@class='select2-result-sub']/li[2]")
    TP_CHECKIN_FIELD = (By.XPATH, "//input[@id='checkin']")
    TP_CHECKOUT_FIELD= (By.XPATH, "//input[@id='checkout']")
    TP_CALENDAR_PICKER_IN = (By.XPATH, "//div[@id='datepickers-container']/div[1]/div/div/div[2]/div[32]")
    TP_CALENDAR_PICKER_OUT = (By.XPATH, "//div[@id='datepickers-container']/div[2]/div/div/div[2]/div[9]")
    TP_CALENDAR_NEXT_BTN = (By.XPATH, "//div[@id='datepickers-container']/div[2]/nav/div[3]")
    TP_GROUP_INCREMENT_BTN = (By.XPATH, "//div[@class='col 01']//button[1]")
    TP_SEARCH_BTN = (By.XPATH, "//div[@id='hotels']//button[@type='submit']")
    TP_COOKIE_BTN = (By.XPATH, "//button[@class='cc-btn cc-dismiss']")