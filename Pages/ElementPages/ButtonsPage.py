import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ButtonPage(BasePage):
    Button_cta = (By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-4']")
    Double_click = (By.XPATH, '//button[@id = "doubleClickBtn"]')
    Right_click = (By.XPATH, '//button[@id = "rightClickBtn"]')
    Click_me = (By.XPATH, "//button[@id='gHxew']")


    def button_page(self):
        self.click(self.Button_cta)
        self.scroll_and_right_click(self.Right_click)
        self.scroll_and_press_escape()
        self.scroll_and_double_click_with_delay(self.Button_cta)
        self.scroll_to_and_click(self.Click_me)