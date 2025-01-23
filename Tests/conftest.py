import pytest
from selenium import webdriver
from Utilities.read_config import read_configuration
from Utilities.logger_config import take_screenshots_on_failure, logger
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Add command-line options to select browser, URL, and headless mode
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser: chrome, firefox, safari")
    parser.addoption("--url", default="default", help="Choose URL: default or dropqa_testing")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")


# Fixture to return the selected browser type
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Fixture to return the appropriate base URL based on the selected environment
@pytest.fixture(scope="session")
def url(request):
    # Read the URL from the command line argument or default
    environment = request.config.getoption("--url")
    base_url = read_configuration(environment, 'BaseURL')  # Dynamic BaseURL reading based on argument
    if not base_url:
        raise ValueError(f"Base URL not found for environment: {environment}")
    return base_url


# Fixture to initialize and quit the driver for each test
@pytest.fixture(scope="function")
def driver(request, browser, url):
    # Initialize the webdriver based on the selected browser
    headless = request.config.getoption("--headless")
    driver = None

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        logger.info("Initialized Chrome browser")

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        logger.info("Initialized Firefox browser")

    elif browser == "safari":
        driver = webdriver.Safari()
        logger.info("Initialized Safari browser")
    else:
        raise Exception(f"Invalid browser specified: {browser}. Use 'chrome', 'firefox', or 'safari'.")

    # Open the dynamic URL provided by the URL fixture
    driver.get(url)
    driver.refresh()
    driver.maximize_window()

    yield driver  # Test will execute after this point

    # Teardown: Quit the driver after test completion
    logger.info("Closing browser")
    driver.quit()


# Hook to capture a screenshot in case of failure during the test execution
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            screenshot_path = take_screenshots_on_failure(driver, item.name)
            logger.info(f"Screenshot captured on failure: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
