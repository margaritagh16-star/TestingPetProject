from pages.base_page import BasePage

class HomePage(BasePage):
    ELEMENTS = "text=Elements"
    ALERTS_WINDOWS = "text=Alerts, Frame & Windows"
    WIDGETS = "text=Widgets"
    PRACTICE_FORM = "text=Forms"
    INTERACTIONS = "text=Interactions"

    def open_alerts_windows(self):
        self.click(self.ALERTS_WINDOWS)

    def open_widgets(self):
        self.click(self.WIDGETS)

    def open_practice_form(self):
        self.click(self.PRACTICE_FORM)

    def open_interactions(self):
        self.click(self.INTERACTIONS)
