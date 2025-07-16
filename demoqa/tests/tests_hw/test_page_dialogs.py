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


# def test_navigation_modal(browser):
#     modal_page = ModalDialogsPage(browser)
#     demo_page = DemoQA(browser)
#     modal_page.visit()
#     modal_page.refresh()
#     modal_page.icon.click()
#     modal_page.back()
#     browser.set_window_size(900, 400)
#     print("Window size set to 900x400")
#     modal_page.forward()
#     current_url = browser.current_url
#     print(f"Current URL: {current_url}")
#     assert current_url == 'https://demoqa.com/'
#     current_title = browser.title
#     print(f"Current title: {current_title}")
#     assert current_title == 'DEMOQA'
#     browser.set_window_size(1000, 1000)
#     print("Window size reset to 1000x1000")