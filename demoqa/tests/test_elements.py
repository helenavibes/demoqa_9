from pages.elements_page import ElementsPage
import time

def test_first_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    time.sleep(2)
    assert elements_page.btn_first_menu.check_count_elements(count=9)
    elements = elements_page.btn_first_menu.find_elements()
    print(f"Found {len(elements)} menu items")