from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utilities.TestData.ElementsTestData.FomTestData import FormtestData
import pytest


@pytest.mark.demo
class TextboxPage(BasePage, FormtestData):
    Element_page = (By.XPATH, "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']")
    Text_box = (By.XPATH, "//div[@class = 'element-list collapse show']//li[@id ='item-0']")
    Full_name_field = (By.XPATH, "//input[@id = 'userName']")
    Email_field = (By.XPATH, "//input[@id = 'userEmail']")
    Address_field = (By.XPATH, "//textarea[@id='currentAddress']")
    Current_address = (By.XPATH, "//textarea[@id='permanentAddress']")

    def click_on_text_box(self):
        self.scroll_to_and_click(self.Element_page)

    def send_keys_on_name(self):
        self.scroll_to_and_click(self.Text_box)
        self.send_keys(self.Full_name_field, FormtestData.fullname)
        self.send_keys(self.Email_field, FormtestData.email)
        self.send_keys(self.Address_field, FormtestData.address)
        self.send_keys(self.Current_address, FormtestData.permanenet_address)
