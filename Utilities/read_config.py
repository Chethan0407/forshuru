from configparser import ConfigParser
import os


def read_configuration(category, key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '..', 'config', 'config.ini')

    # Ensure the config file exists
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    config = ConfigParser()
    config.read(config_path)

    # Check if the category and key exist in the config file
    if not config.has_section(category):
        raise ValueError(f"Section '{category}' not found in the config file")
    if not config.has_option(category, key):
        raise ValueError(f"Key '{key}' not found in section '{category}' of the config file")

    # Return the value for the key
    return config.get(category, key)


from selenium.webdriver.common.by import By
from Pages.BasePage import basePage


class SamplePage(basePage):
    Invalid_Email_Error = (By.XPATH, "//span[contains(text(), 'The e-mail address entered is invalid.')]")

    def assert_email_invalid_error_not_displayed(self):
        elements = self.find_elements(self.Invalid_Email_Error)

        # Assert that the error message is NOT present or visible
        assert not elements, "The email invalid message is displayed, which is incorrect."
        print("The email invalid message is NOT displayed as expected.")
