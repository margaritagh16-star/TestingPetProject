import pytest
from pages.alerts_page import AlertsPage

def test_alert_accept(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_alert()
    # Если alert был просто информационный — тест проходит если не упал

def test_timer_alert(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_timer_alert()
    # Можно добавить ожидание или проверку состояния

def test_confirm_ok(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_confirm(accept=True)
    assert "You selected Ok" in alerts.get_confirm_result()

def test_confirm_cancel(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_confirm(accept=False)
    assert "You selected Cancel" in alerts.get_confirm_result()

def test_prompt_accept_with_text(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_prompt(text="Hello!")
    assert "Hello!" in alerts.get_prompt_result()

def test_prompt_cancel(page):
    page.goto("https://demoqa.com/alerts")

    alerts = AlertsPage(page)
    alerts.trigger_prompt(text="ignored", accept=False)
    # В DemoQA prompt-результат может быть пустым или другим
    assert alerts.get_prompt_result() != ""
