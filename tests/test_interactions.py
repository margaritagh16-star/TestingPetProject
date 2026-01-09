from pages.interactions_page import InteractionsPage

def test_interactions_navigation(page):
    page.goto("https://demoqa.com/interaction")
    i = InteractionsPage(page)
    i.open_droppable()
    i.open_resizable()
    i.open_sortable()
