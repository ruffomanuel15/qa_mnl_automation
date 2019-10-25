import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestPhpTravels(object):
    def test_php_travels(self):
        self.driver.get(env.page_url)
        on.PhpTravels.is_title_matches(self)
        on.PhpTravels.go_to_featured_tours(self)
        on.PhpTravels.featured_tours_info(self)
        on.PhpTravels.screenshot(self)