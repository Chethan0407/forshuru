from Pages.ElementPages.RadiobuttonPage import RadioButtonPage
from Pages.ElementPages.TextBoxPage import TextboxPage
import pytest


class TestRadioButton:
    @pytest.mark.demo
    @pytest.mark.usefixtures("driver")
    def test_radio_buttom(self, driver):
        test_box = TextboxPage(driver)
        test_box.click_on_text_box()
        radio = RadioButtonPage(driver)
        radio.radio_button_actions()