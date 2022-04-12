from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def wait_for_element_present(self, locator, time_out_sec=10):
        use_locator = self.locator_type(locator)
        element = WebDriverWait(self.driver, time_out_sec).until(
            EC.presence_of_element_located((use_locator, locator)))
        return element

    def _find_element(self, locator, time_out_sec=10):
        return self.wait_for_element_present(locator, time_out_sec)

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def enter_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def delete_element(self, locator):
        element = self._find_element(locator)
        element.clear()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")