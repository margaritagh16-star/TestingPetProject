from pages.base_page import BasePage

class ElementsPage(BasePage):

    TEXT_BOX = "text=Text Box"
    CHECK_BOX = "text=Check Box"
    BUTTONS = "text=Buttons"

    def open_text_box(self):
        self.click(self.TEXT_BOX)

    def open_check_box(self):
        self.click(self.CHECK_BOX)

    def open_buttons(self):
        self.click(self.BUTTONS)
