from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AlertPage(BasePage):
    Alerts_cta = (By.XPATH, "//h5[normalize-space() ='Alerts, Frame & Windows'] ")
    Alert_second_cta = (By.XPATH, "//span[normalize-space()='Alerts'] ")
    Click_me_cta = (By.XPATH, "//button[@id = 'alertButton']")
    Alert_appear_after_five_sec = (By.XPATH, "//button[@id = 'timerAlertButton']")

    def alert_cta_click(self):
        self.scroll_to_and_click(self.Alerts_cta)
        self.scroll_to_and_click(self.Alert_second_cta)
        self.scroll_to_and_click(self.Click_me_cta)

    def accept_alert__popup(self):
        self.accept_alert()

    def alert_appear_after_five_sec(self):
        self.scroll_to_and_click(self.Alert_appear_after_five_sec)
        self.accept_alert()
