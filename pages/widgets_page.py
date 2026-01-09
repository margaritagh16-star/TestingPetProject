from pages.base_page import BasePage

class WidgetsPage(BasePage):

    ACCORDION_TAB = "text=Accordian"
    DATE_PICKER = "text=Date Picker"
    PROGRESS_BAR = "text=Progress Bar"
    SLIDER = "text=Slider"
    TOOL_TIPS = "text=Tool Tips"

    def open_accordion(self):
        self.click(self.ACCORDION_TAB)

    def open_date_picker(self):
        self.click(self.DATE_PICKER)

    def open_progress_bar(self):
        self.click(self.PROGRESS_BAR)

    def open_slider(self):
        self.click(self.SLIDER)

    def open_tool_tips(self):
        self.click(self.TOOL_TIPS)
