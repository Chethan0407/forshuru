import logging
import os
from datetime import datetime

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a logs directory if it doesn't exist
log_dir = "/Users/chethangopal/Desktop/NewSelenium/Tests/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, 'Automation.log')

# File Handler (Append mode)
fh = logging.FileHandler(log_file_path, mode='a')  # Append mode ('a') to append logs
fh.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt="%y-%d-%m %H:%M:%S %p")
fh.setFormatter(formatter)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def take_screenshots_on_failure(driver, failure_screenshot_name):
    """
    Capture a screenshot when a test fails.
    :param driver: WebDriver instance
    :param failure_screenshot_name: Test failure name
    :return: Screenshot path
    """
    screenshot_dir = os.path.join(log_dir, 'FailedTest_PageScreenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Create a timestamped screenshot name
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_dir, f'{failure_screenshot_name}_{timestamp}.png')

    try:
        driver.save_screenshot(screenshot_path)
        logger.info(f'Screenshot saved at: {screenshot_path}')
    except Exception as e:
        logger.error(f'Failed to take screenshot: {e}')

    return screenshot_path


# Function to return the logger for use in other modules
def configure_logger():
    return logger
