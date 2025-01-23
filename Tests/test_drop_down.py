

from Pages.HerokuPage.DropDown import DropDownPage
import pytest


class TestDropDown:
    @pytest.mark.usefixtures("driver")
    @pytest.mark.heroku
    def test_drop_down(self, driver):
        drop_down = DropDownPage(driver)
        drop_down.click_drop_down_cta()
        drop_down.select_tab_click()
        drop_down.select_option1()
