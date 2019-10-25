import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class LoginPage(object):
    def test_login_to_cms(self):
        self.driver.get(env.page_url)
        on.OpenSourceDemo.login_to_cms(self)

