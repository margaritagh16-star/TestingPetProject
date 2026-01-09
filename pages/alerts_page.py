from pages.base_page import BasePage

class AlertsPage(BasePage):

    ALERT_BUTTON = "#alertButton"
    TIMER_ALERT_BUTTON = "#timerAlertButton"
    CONFIRM_BUTTON = "#confirmButton"
    PROMPT_BUTTON = "#promtButton"
    CONFIRM_RESULT = "#confirmResult"
    PROMPT_RESULT = "#promptResult"

    def trigger_alert(self):
        # Регистрация обработчика перед кликом
        self.handle_dialog(accept=True)
        self.click(self.ALERT_BUTTON)

    def trigger_timer_alert(self):
        # alert появляется через 5 секунд после клика
        self.handle_dialog(accept=True)
        self.click(self.TIMER_ALERT_BUTTON)

    def trigger_confirm(self, accept=True):
        # accept=True → OK, accept=False → Cancel
        self.handle_dialog(accept=accept)
        self.click(self.CONFIRM_BUTTON)

    def trigger_prompt(self, text=None, accept=True):
        # ввод текста в prompt и подтверждение
        self.handle_dialog(accept=accept, prompt_text=text)
        self.click(self.PROMPT_BUTTON)

    def get_confirm_result(self):
        return self.get_text(self.CONFIRM_RESULT)

    def get_prompt_result(self):
        return self.get_text(self.PROMPT_RESULT)
