import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestClothingShop(object):
    def test_clothingshop(self):
        self.driver.get(env.page_url)
        on.ClothingShop.is_title_matches(self)
        # clothingShop code is ran for every tab
        on.ClothingShop.assertion_tests(self, "Popular")
        on.ClothingShop.assertion_tests(self, "Best Sellers")
