import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestPhpTravels(object):
    def test_php_travels(self):
        self.driver.get(env.page_url)
        on.PhpTravelSearch.is_title_matches(self)
        on.PhpTravelSearch.hotels_tab(self)
        on.PhpTravelSearch.search_travel_package(self)
        on.PhpTravelSearch.screenshot(self)