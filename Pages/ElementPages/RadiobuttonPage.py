from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import re


class RadioButtonPage(BasePage):
    Radio_Button_cta =( By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-2']")
    Yes_Radio_Button = (By.XPATH, "//label[@for='yesRadio']")
    Imressive_button = (By.XPATH, "//label[@for='impressiveRadio']")
    No_raido_button = (By.XPATH, "//input[@id = 'noRadio']")
    Actual_text_element = (By.XPATH, "//p[@class='mt-3']")


    def radio_button_actions(self):
        self.scroll_to_and_click(self.Radio_Button_cta)
        self.scroll_to_and_click(self.Yes_Radio_Button)
        actual_text = self.get_element_text(self.Actual_text_element)
        assert re.match(r"You have selected Yes", actual_text)


        self.scroll_to_and_click(self.Imressive_button)
        actual_text = self.get_element_text(self.Actual_text_element)
        assert re.match(r"You have selected Impressive", actual_text)



