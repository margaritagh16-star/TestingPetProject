from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):

    NEW_TAB_BTN = "#tabButton"
    NEW_WINDOW_BTN = "#windowButton"
    NEW_WINDOW_MESSAGE_BTN = "#messageWindowButton"
    BODY_TEXT = "body"

    def open_new_tab(self):
        self.click(self.NEW_TAB_BTN)

    def open_new_window(self):
        self.click(self.NEW_WINDOW_BTN)

    def open_new_window_message(self):
        self.click(self.NEW_WINDOW_MESSAGE_BTN)

    def get_body_text(self):
        return self.get_text(self.BODY_TEXT)
