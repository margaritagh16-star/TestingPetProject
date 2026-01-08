from pages.elements_page import ElementsPage
from pages.buttons_page import ButtonsPage

def test_double_click(page):
    page.goto("https://demoqa.com/elements")

    elements = ElementsPage(page)
    elements.open_buttons()

    buttons = ButtonsPage(page)
    buttons.double_click()

    assert "You have done a double click" in buttons.get_message()
