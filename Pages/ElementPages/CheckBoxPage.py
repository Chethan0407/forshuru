from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Checkbox(BasePage):
    CheckBox_CTA = (By.XPATH, "//span[normalize-space() = 'Check Box']")
    CheckBox_click = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
    Expand_button = (By.XPATH, "//button[@title='Expand all']//*[name()='svg']")
    Collapse_all = (By.XPATH, "//button[@title='Collapse all']//*[name()='svg']")

    def calling_check_box(self):
        self.scroll_to_and_click(self.CheckBox_CTA)
        self.scroll_to_and_click(self.CheckBox_click)
        self.scroll_to_and_click(self.Expand_button)
        self.scroll_to_and_click(self.Collapse_all)
