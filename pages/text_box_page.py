from pages.base_page import BasePage

class TextBoxPage(BasePage):

    FULL_NAME = "#userName"
    EMAIL = "#userEmail"
    CURRENT_ADDRESS = "#currentAddress"
    PERMANENT_ADDRESS = "#permanentAddress"
    SUBMIT = "#submit"
    OUTPUT = "#output"

    def fill_form(self, name, email, current_address, permanent_address):
        self.fill(self.FULL_NAME, name)
        self.fill(self.EMAIL, email)
        self.fill(self.CURRENT_ADDRESS, current_address)
        self.fill(self.PERMANENT_ADDRESS, permanent_address)

    def submit(self):
        self.click(self.SUBMIT)

    def get_output(self):
        return self.get_text(self.OUTPUT)
