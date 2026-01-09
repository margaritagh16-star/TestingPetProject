from pages.base_page import BasePage

class InteractionsPage(BasePage):

    DROPPABLE_TAB = "text=Droppable"
    RESIZABLE_TAB = "text=Resizable"
    SORTABLE_TAB = "text=Sortable"
    SELECTABLE_TAB = "text=Selectable"

    def open_droppable(self):
        self.click(self.DROPPABLE_TAB)

    def open_resizable(self):
        self.click(self.RESIZABLE_TAB)

    def open_sortable(self):
        self.click(self.SORTABLE_TAB)

    def open_selectable(self):
        self.click(self.SELECTABLE_TAB)
