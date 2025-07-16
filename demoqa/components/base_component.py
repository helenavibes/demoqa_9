from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self) -> WebElement:
        return self.driver.find_element(*self.locator)

    def get_text(self) -> str:
        return str(self.find_element().text)