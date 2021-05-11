""" SITE CONSTANTS GO HERE """

from pages import loginPage as lp, \
    letskodeitPage as lk, \
    clothingShop as cs
    # samplePage as smp, \


class Pages(object):
    LoginPage = lp.LoginPage
    LetsKodeIt = lk.LetsKodeIt
    ClothingShop = cs.ClothingShop
  #  SamplePage = smp.SamplePage

# ENVIRONMENT
environments = {
    'KODE'   : 'https://learn.letskodeit.com/p/practice',
    'CLOT'    : 'http://automationpractice.com/index.php',
    'STG'   : 'https://sit:SS19pro!@staging.adidas-style.com',
    'PROD'  : 'https://www.adidas-style.com'
}
page_url = environments['KODE']
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

