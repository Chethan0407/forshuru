from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.heroku
class DragAndDrop(BasePage):
    drag_and_drop_cta = (By.XPATH, '//a[@href="/drag_and_drop"]')
    source = (By.XPATH, "//div[@id = 'column-a']")
    target = (By.XPATH, "//div[@id = 'column-b']")

    def cta_click(self):
        self.click(self.drag_and_drop_cta)

    def perform_drag_and_drop(self):
        self.drag_and_drop(self.source, self.target)

    def get_source_text(self):
        return self.find_element(self.source).text

    def get_target_text(self):
        return self.find_element(self.target).text

    # this is for page action demow qa


@pytest.mark.demo
class DemoDragAndDrop(BasePage):
    # Locators for demoqa drag and drop
    Interaction_cta = (By.XPATH, "//div[@class='card-body']//h5[text()='Interactions']")
    Dropable_cta = (By.XPATH, "//span[normalize-space()='Droppable']")  # Removed the extra space
    Drag_s = (By.XPATH, '//div[@id = "draggable"]')
    Drop_t = (By.XPATH, "//div[@id = 'simpleDropContainer']//div[@id='droppable']")
    elements_section = (By.XPATH, "//div[@class='card'][contains(., 'Elements')]")

    def click_on_integration(self):
        self.scroll_to_and_click(self.Interaction_cta)

    def click_on_draggble_cta(self):
        self.scroll_to_and_click(self.Dropable_cta)

    def perform_drag_and_drop_demo(self):
        # Correcting the drag and drop method to use the correct target locator
        self.drag_and_drop(self.Drag_s, self.Drop_t)  # Use Drop_t as the target
