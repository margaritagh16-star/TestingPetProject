from pages.widgets_page import WidgetsPage

def test_widgets_navigation(page):
    page.goto("https://demoqa.com/widgets")
    w = WidgetsPage(page)
    w.open_accordion()
    w.open_tool_tips()
