from pages.alerts_windows_page import AlertsWindowsPage

def test_alerts(page):
    page.goto("https://demoqa.com/alertsWindows")
    aw = AlertsWindowsPage(page)
    aw.click_alert()
    assert page.get_dialog_message()  # зависит от реализации
