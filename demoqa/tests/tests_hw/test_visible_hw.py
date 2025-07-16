import time
import pytest
from pages.accordion import Accordion


@pytest.mark.parametrize('expected_text', [
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
])
def test_visible_accordion(browser, expected_text):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.section1_content.is_displayed()
    assert expected_text in accordion_page.section1_content.get_text()
    accordion_page.section1_heading.click()
    time.sleep(2)
    assert not accordion_page.section1_content.is_displayed()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.section2_content_p1.is_displayed()
    assert not accordion_page.section2_content_p2.is_displayed()
    assert not accordion_page.section3_content.is_displayed()