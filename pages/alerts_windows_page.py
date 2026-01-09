from pages.base_page import BasePage

class AlertsWindowsPage(BasePage):
    ALERT_BUTTON = "#alertButton"
    TIMER_ALERT_BUTTON = "#timerAlertButton"
    CONFIRM_BUTTON = "#confirmButton"
    PROMPT_BUTTON = "#promtButton"
    CONFIRM_RESULT = "#confirmResult"
    PROMPT_RESULT = "#promptResult"

    def click_alert(self):
        self.click(self.ALERT_BUTTON)

    def click_timer_alert(self):
        self.click(self.TIMER_ALERT_BUTTON)

    def click_confirm(self):
        self.click(self.CONFIRM_BUTTON)

    def click_prompt(self):
        self.click(self.PROMPT_BUTTON)

    def get_confirm_result(self):
        return self.get_text(self.CONFIRM_RESULT)

    def get_prompt_result(self):
        return self.get_text(self.PROMPT_RESULT)
