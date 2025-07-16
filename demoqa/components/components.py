from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    def __init__(self, driver, locator, timeout=10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def click(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator))
        )
        element.click()

    def get_text(self):
        return self.find_element().text

    def exist(self):
        try:
            self.find_element()
            return True
        except:
            return False

    def is_displayed(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        try:
            elements = self.find_elements()
            return len(elements) == count
        except:
            return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)