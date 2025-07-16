from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.get_url()
    demo_qa_page.btn_elements.click()
    elements_page.visit()
    assert elements_page.get_url()