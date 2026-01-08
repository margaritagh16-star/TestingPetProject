from pages.elements_page import ElementsPage
from pages.text_box_page import TextBoxPage

def test_text_box_form(page):
    page.goto("https://demoqa.com/elements")

    elements = ElementsPage(page)
    elements.open_text_box()

    text_box = TextBoxPage(page)
    text_box.fill_form(
        name="John Doe",
        email="john@test.com",
        current_address="Kyiv",
        permanent_address="Lviv"
    )
    text_box.submit()

    assert "John Doe" in text_box.get_output()
