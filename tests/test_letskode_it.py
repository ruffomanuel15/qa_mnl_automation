import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestLetsKodeIt(object):
    def test_tablepage(self):
        self.driver.get(env.page_url)
        on.LetsKodeit.is_title_matches(self)
        on.LetsKodeit.assertion_tests(self)

