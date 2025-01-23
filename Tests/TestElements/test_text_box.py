import pytest
from Pages.ElementPages.TextBoxPage import TextboxPage


class TestTextBox:
    @pytest.mark.demo
    @pytest.mark.usefixtures("driver")
    def test_test_box(self, driver):
        test_box = TextboxPage(driver)
        test_box.click_on_text_box()
        test_box.send_keys_on_name()
