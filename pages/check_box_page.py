from pages.base_page import BasePage

class CheckBoxPage(BasePage):

    EXPAND_ALL = ".rct-option-expand-all"
    NOTES_CHECKBOX = "label[for='tree-node-notes']"
    RESULT = "#result"

    def expand_all(self):
        self.click(self.EXPAND_ALL)

    def select_notes(self):
        self.click(self.NOTES_CHECKBOX)

    def get_result(self):
        return self.get_text(self.RESULT)
