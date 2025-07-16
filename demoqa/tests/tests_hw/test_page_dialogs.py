import time
from pages.modal_dialogs import ModalDialogsPage
from pages.demoqa import DemoQA
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_elements(browser):
    modal_page = ModalDialogsPage(browser)
    print(f"Base URL before visit: {modal_page.base_url}")
    modal_page.visit()
    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located(('css selector', '.btn'))
    )
    assert modal_page.buttons.check_count_elements(count=5)

    buttons = modal_page.buttons.find_elements()
    print(f"Found {len(buttons)} buttons on the page")
    for i, button in enumerate(buttons, 1):
        print(f"Button {i}: {button.text}")
