# DropDownPage.py
from Pages.BasePage import BasePage  # Correctly importing BasePage
from selenium.webdriver.common.by import By


class DropDownPage(BasePage):
    Drop_Down_CTA = (By.XPATH, '//a[@href = "/dropdown"]')
    Select_Tab = (By.XPATH, "//select[@id='dropdown']")
    Option_1 = (By.XPATH, "//select[@id='dropdown']/option[text()='Option 1']")
    Option_2 = (By.XPATH, "//select[@id='dropdown']/option[text()='Option 2']")

    def click_drop_down_cta(self):
        self.click(self.Drop_Down_CTA)

    def select_tab_click(self):
        self.click(self.Select_Tab)

    def select_option1(self):
        self.click(self.Option_1)
