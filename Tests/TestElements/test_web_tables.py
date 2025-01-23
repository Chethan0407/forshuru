from Pages.ElementPages.WebtablesPage import WebtablesPage
from Pages.ElementPages.TextBoxPage import TextboxPage
import pytest


class TestWebtables:
    @pytest.mark.demo
    @pytest.mark.usefixtures("driver")
    def test_web_tables(self, driver):
        test_box = TextboxPage(driver)
        test_box.click_on_text_box()
        webtable = WebtablesPage(driver)
        webtable.web_table_page()
        webtable.web_table_edit()
        # webtable.Delete_record()
