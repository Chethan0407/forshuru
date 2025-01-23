from Pages.HerokuPage.DragAndDrop import DragAndDrop, DemoDragAndDrop
import pytest


class TestDragAndDrop:

    @pytest.mark.heroku
    def test_drag_and_drop(self, driver):
        drag_and_drop_page = DragAndDrop(driver)
        drag_and_drop_page.cta_click()
        drag_and_drop_page.perform_drag_and_drop()
        drag_and_drop_page.get_source_text()
        drag_and_drop_page.get_target_text()

    @pytest.mark.demo
    def test_demo_drag_and_drop(self, driver):
        demo_drag_and_drop = DemoDragAndDrop(driver)
        demo_drag_and_drop.click_on_integration()
        demo_drag_and_drop.click_on_draggble_cta()
        demo_drag_and_drop.perform_drag_and_drop_demo()
