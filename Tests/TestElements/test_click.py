import time

import pytest
from Pages.ElementPages.TextBoxPage import TextboxPage
from Pages.ElementPages.ButtonsPage import ButtonPage


class TestCheckBox:

    @pytest.mark.demo
    @pytest.mark.usefixtures("driver")
    def test_check_box(self, driver):
        test_box = TextboxPage(driver)
        test_box.click_on_text_box()
        button = ButtonPage(driver)
        button.button_page()




