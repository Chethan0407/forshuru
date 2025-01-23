import logging
from selenium.common import NoSuchElementException
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='automation_tests.log',  # You can log this to a file as well
    filemode='w'  # Overwrite log file each time
)
logger = logging.getLogger()

class CheckBoxPage(BasePage):
    CheckBox_Cta = (By.XPATH, "//a[@href='/checkboxes']")
    CheckBox1 = (By.XPATH, "//input[@type='checkbox'][1]")
    CheckBox2 = (By.XPATH, "//input[@type='checkbox'][2]")
    checkbox_assert = (By.TAG_NAME, "h3")

    def click_on_check_box_cta(self):
        logger.info("Attempting to click on the checkbox CTA")
        try:
            self.click(self.CheckBox_Cta)
            logger.info("Successfully clicked on the checkbox CTA")
        except NoSuchElementException:
            logger.error("Checkbox CTA button not found.")
            raise

    def double_click_on_checkbox_one(self):
        logger.info("Attempting to double click on checkbox 1")
        try:
            self.double_click_with_delay(self.CheckBox1)
            logger.info("Successfully double-clicked on checkbox 1")
        except NoSuchElementException:
            logger.error("Checkbox 1 not found.")
            raise

    def double_click_on_checkbox_two(self):
        logger.info("Attempting to double click on checkbox 2")
        try:
            self.double_click_with_delay(self.CheckBox2)
            logger.info("Successfully double-clicked on checkbox 2")
        except NoSuchElementException:
            logger.error("Checkbox 2 not found.")
            raise

    def asserting_header(self):
        expected_text = "Checkboxes"
        logger.info("Verifying page header text")
        try:
            page_header = self.find_element(self.checkbox_assert)
            if page_header.text == expected_text:
                logger.info("Page header verified successfully.")
            else:
                logger.warning(f"Page header mismatch. Expected: {expected_text}, Found: {page_header.text}")
        except NoSuchElementException:
            logger.error("Page header element not found.")
            raise
