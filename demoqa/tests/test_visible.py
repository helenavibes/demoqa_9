import time
from pages.elements_page import ElementsPage

def test_visible_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.is_displayed()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.is_displayed()
