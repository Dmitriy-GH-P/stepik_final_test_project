from .pages.main_page import MainPage                # Запуск теста через терминал pytest -v --tb=line --language=en test_main_page.py


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()