from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime

class Base(object):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout


class Waiters(Base):

    @classmethod
    def wait_for_it(cls, timeout):
        """sets the condition to an exact time period to wait"""
        return time.sleep(timeout)

    @classmethod
    def wait_for_visible(cls, selector, timeout=5):
        wait = WebDriverWait(cls, timeout)
        msg = ('%s should be visible' % selector)
        wait.until(EC.visibility_of(selector), message=msg)

    @classmethod
    def wait_for_present(cls, selector, timeout=5):
        """checking that there is at least one element present on a web page"""
        wait = WebDriverWait(cls, timeout)
        msg = ('%s should be present' % selector)
        wait.until(EC.presence_of_all_elements_located, message=msg)


class Commands(Base):

    def take_screenshot(self, test):
        x = datetime.today()
        date = x.ctime()
        name = test

        self.save_screenshot('results/screenshots/' + str(name) + '_' + str(date) + '_.png')
        return test

    @classmethod
    def is_clickable(cls, selector):
        selector.is_displayed() and selector.is_enabled(), "Selector " + str(selector) + "is not clickable"


    @classmethod
    def is_visible(cls, selector):
        msg = ('Element is not visible', selector)
        return selector.is_displayed(), msg

    @classmethod
    def if_visible_click(cls, selector, timeout=5):
        """clicks on element if present on the page"""
        WebDriverWait(cls, timeout).until(EC.visibility_of_element_located(selector)).click()

    @classmethod
    def if_visible_click_xpath(cls, selector, timeout=5):
        """clicks on element defined by xpath selector if visible"""
        WebDriverWait(cls, timeout).until(EC.visibility_of_element_located((By.XPATH, selector))).click()

    @classmethod
    def text_is_present_in_element(cls, selector):
        """Asserts that text is present in a element using the selenium element object"""
        elem_text = selector.text
        assert elem_text is not None, "element text is None"
        assert len(elem_text) > 1, "element text is empty"

    def hover_over_element(self, selenium,  selector):
        """hovers over element defined by selector"""
        msg = ('located by: %s element: %s should be present' % selector)
        temp = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located(selector), message=msg)  # locate account menu
        ActionChains(selenium).move_to_element(temp).perform()
