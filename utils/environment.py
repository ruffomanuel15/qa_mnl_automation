""" SITE CONSTANTS GO HERE """

from pages import loginPage as lp,\
    clothingShop as cs,\
    phpTravels as pt
    # pagefile as xx

class Pages(object):
    LoginPage = lp.LoginPage
    ClothingShop = cs.ClothingShop
    PHPTravels = pt.PHPTravelsPage
  #  SamplePage = smp.SamplePage

# ENVIRONMENT
environments = {
    'Dev'   : 'https://admin:idm[Ey^7qruTnZvV@ao-sit-dev.codeandtheory.net',
    'QA'    : 'https://admin:idm[Ey^7qruTnZvV@ao-sit-qa.codeandtheory.net',
    'STG'   : 'https://www.google.com/',
    'PROD'  : 'https://www.adidas-style.com',
    'PRAC'  : 'https://learn.letskodeit.com/p/practice',
    'SHOP'  : 'http://automationpractice.com/index.php',
    'PHPTRAVELS'    : 'https://www.phptravels.net/'
}
page_url = environments['PHPTRAVELS']
force_logout = page_url+'/user/logout'



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
