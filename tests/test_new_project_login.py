import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestProjectLogin(object):
    def test_successful_login(self):
        self.driver.get(env.page_url)

        #on.LoginPage.login_as_standard_user(self)
        on.LoginPage.search_test(self)
        on.LoginPage.screenshot(self)