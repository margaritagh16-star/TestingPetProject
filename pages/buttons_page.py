from pages.base_page import BasePage

class ButtonsPage(BasePage):

    DOUBLE_CLICK_BTN = "#doubleClickBtn"
    MESSAGE = "#doubleClickMessage"

    def double_click(self):
        self.page.locator(self.DOUBLE_CLICK_BTN).dblclick()

    def get_message(self):
        return self.get_text(self.MESSAGE)
