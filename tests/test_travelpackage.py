import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestTravelPackage(object):
    def test_add_to_cart(self):
        self.driver.get(env.page_url)
        on.TravelPackage.is_title_matches(self)
        on.TravelPackage.dest(self)
        on.TravelPackage.take_screenshot(self)
