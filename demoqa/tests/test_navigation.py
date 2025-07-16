from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    # Теперь можно использовать методы страницы
    demo_qa_page.visit()

    # Пример проверок навигации
    initial_url = demo_qa_page.get_url()

    # Переходим на другую страницу
    demo_qa_page.btn_elements.click()
    new_url = demo_qa_page.get_url()
    assert new_url != initial_url

    # Используем методы навигации браузера
    demo_qa_page.back()
    assert demo_qa_page.get_url() == initial_url

    demo_qa_page.forward()
    assert demo_qa_page.get_url() == new_url

    demo_qa_page.refresh()
    assert demo_qa_page.get_url() == new_url