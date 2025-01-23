from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, timeout=self.timeout).until(ec.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = WebDriverWait(self.driver, timeout=10).until(ec.element_to_be_clickable(locator))
        element.click()

    def clear(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        element.clear()

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, timeout=10).until(ec.element_to_be_clickable(locator))
        element.send_keys(text)

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, timeout=10).until((ec.alert_is_present()))
        self.driver.switch_to.alert.dismiss()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()

    def scroll_and_double_click_with_delay(self, locator, delay=0.5):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        self.actions.move_to_element(element).click().pause(delay).click().perform()

    def switch_to_frame(self, locator):
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()

    def scroll_to_elemet(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_to_and_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator)).click()

    def javascript_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def left_click(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def scroll_and_right_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def scroll_and_press_escape(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
