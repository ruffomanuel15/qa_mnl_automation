import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestClothingShop(object):
    def test_add_to_cart(self):
        self.driver.get(env.page_url)
        on.ClothingShop.is_title_matches(self)
        on.ClothingShop.add_to_cart(self)
        on.ClothingShop.take_screenshot(self)
