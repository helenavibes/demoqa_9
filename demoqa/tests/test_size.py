import time
from pages.demoqa import DemoQA

def test_size(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    browser.set_window_size(1000, 1000)
    time.sleep(2)
    browser.set_window_size(1000, 1000)