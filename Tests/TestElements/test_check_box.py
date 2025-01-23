from Pages.ElementPages.CheckBoxPage import Checkbox
from Pages.ElementPages.TextBoxPage import TextboxPage

import pytest

class TestCheckBo():
        @pytest.mark.demo
        @pytest.mark.usefixtures("driver")
        def test_test_box(self, driver):
            test_box = TextboxPage(driver)
            test_box.click_on_text_box()
            checkbox = Checkbox(driver)
            checkbox.calling_check_box()