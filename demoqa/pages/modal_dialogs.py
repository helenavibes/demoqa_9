from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, base_url)

        self.buttons = WebElement(driver, '.btn')
        self.icon = WebElement(driver, 'header a')
