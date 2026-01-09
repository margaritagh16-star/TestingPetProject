import pytest


from pages.date_picker_page import DatePickerPage

def test_select_date(page):
    dp = DatePickerPage(page)
    dp.open()

    dp.select_date("10 Jul 2005")

    # Проверка, что значение было установлено
    assert "10 Jul 2005" in dp.get_selected_date()

def test_select_date_time(page):
    dp = DatePickerPage(page)
    dp.open()

    dp.select_date_time("15 Nov 2023 12:30 PM")

    # Проверка результата
    result = dp.get_selected_date_time()
    assert "15 Nov 2023" in result
    assert "12:30 PM" in result
