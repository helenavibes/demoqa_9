from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        if self.base_url:
            return self.driver.get(self.base_url)
        raise ValueError("Base URL is not set")

    # def find_element(self, by, value):
    #     return self.driver.find_element(by, value)

    def get_url(self):
        return self.driver.current_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title