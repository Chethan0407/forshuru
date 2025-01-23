import pytest
from Pages.HerokuPage.Checkbox import CheckBoxPage


class TestCheckBox:

    @pytest.mark.heroku
    @pytest.mark.usefixtures("driver")
    def test_check_box(self, driver):
        check_box_text = CheckBoxPage(driver)
        check_box_text.click_on_check_box_cta()
        check_box_text.double_click_on_checkbox_one()
        check_box_text.double_click_on_checkbox_two()
        check_box_text.asserting_header()
