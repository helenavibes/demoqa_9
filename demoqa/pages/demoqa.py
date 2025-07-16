from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement


class DemoQA(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/'
        super().__init__(driver, base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, 'div.card:nth-child(1)')
        self.footer = WebElement(driver, 'footer span')

    def go_to_elements_page(self):
        self.elements_button.find_element().click()

    def exist_icon(self):
        try:
            self.icon.find_element()
            return True
        except NoSuchElementException:
            return False
# class DemoQA(BasePage):
#
#     def __init__(self, driver):
#         self.base_url = 'https://demoqa.com/'
#         super().__init__(driver,self.base_url)
#
#         self.icon = WebElement(driver,'#app > header > a')
#         self.btn_elements = WebElement(driver,'div.card:nth-child(1)')
#
#     def exist(self):
#         try:
#             self.find_element()
#             return True
#         except NoSuchElementException:
#             return False