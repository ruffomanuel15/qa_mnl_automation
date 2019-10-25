import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestPHPTravels(object):
    def test_add_to_cart(self):
        self.driver.get(env.page_url)
        on.PHPTravels.is_title_matches(self)
        on.PHPTravels.featured_tours_details(self)
