""" SITE CONSTANTS GO HERE """

from pages import clothingShop as cs,\
    loginPage as lp, \
    letskodeitPage as lc,\
    phpTravels as pt



# pagefile as xx

class Pages(object):
    ClothingShop = cs.ClothingShop
    LoginPage = lp.LoginPage
    LetsKodeit = lc.LetsKodeItPage
    DressesPage = cs.AddToCart
    PhpTravels = pt.PhpTravels
    PhpTravelSearch = pt.PhpTravelSearch


#  SamplePage = smp.SamplePage

# ENVIRONMENT
environments = {
    'Dev': 'https://admin:idm[Ey^7qruTnZvV@ao-sit-dev.codeandtheory.net',
    'QA': 'https://admin:idm[Ey^7qruTnZvV@ao-sit-qa.codeandtheory.net',
    'STG': 'https://www.google.com/',
    'PROD': 'https://www.adidas-style.com',
    'PRAC': 'https://learn.letskodeit.com/p/practice',
    'SHOP': 'http://automationpractice.com/index.php',
    'PHPTRAVEL': 'https://phptravels.net/'
}
page_url = environments['PHPTRAVEL']
force_logout = page_url + '/user/logout'

# TEST DATA - STAGING & PROD
# STAGING
# Admin User
user = 'admin_auto'
email = 'admin_auto@mailinator.com'
pwd = 'Welcome_123'

# Invalid User
bad_user = 'baduser'
bad_email = 'bademail'
bad_pwd = 'badpwd'

# Sales POC Account (GMAIL)
poc_email = 'qaeautom@gmail.com'
poc_password = 'bluemonkey56'

# PATH TO REPORTS
# results/REPORT_NAME.html .. use --self-contained-html flag to be able to deliver report + styles
