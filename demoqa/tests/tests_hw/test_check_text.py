from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    page = DemoQA(browser)
    page.visit()
    assert page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_center_text_on_elements_page(browser):
    demo_page = DemoQA(browser)
    elements_page = ElementsPage(browser)
    demo_page.visit()
    demo_page.btn_elements.click()
    assert elements_page.central_text.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert  elements_page.icon.exist()
    assert  elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()