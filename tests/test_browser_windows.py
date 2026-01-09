import time
import pytest
from pages.browser_windows_page import BrowserWindowsPage

def test_new_tab_and_window(page):
    page.goto("https://demoqa.com/browser-windows")

    bw = BrowserWindowsPage(page)

    # Открываем новую вкладку
    bw.open_new_tab()

    # Переключиться на новую вкладку
    bw.switch_to_window(1)

    # Проверить что текст появился
    assert bw.get_body_text() != ""  # хоть какой-то текст есть

    # Вернуться в основное окно
    bw.switch_to_window(0)

    # Открываем новое окно
    bw.open_new_window()
    bw.switch_to_window(1)
    assert bw.get_body_text() != ""

def test_new_window_message(page):
    page.goto("https://demoqa.com/browser-windows")

    bw = BrowserWindowsPage(page)

    bw.open_new_window_message()
    bw.switch_to_window(1)

    body_text = bw.get_body_text()
    assert "Knowledge" in body_text or body_text != ""
