import pytest
from Pages.HerokuPage.Alert import AlertPage


class TestAlert:
    @pytest.mark.demo
    @pytest.mark.usefixtures("driver")
    def test_alert_accept(self, driver):
        alert_accept = AlertPage(driver)
        alert_accept.alert_cta_click()
        alert_accept.accept_alert__popup()
        alert_accept.alert_appear_after_five_sec()
