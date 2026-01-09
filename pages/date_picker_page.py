from pages.base_page import BasePage

class DatePickerPage(BasePage):

    DATE_INPUT = "#datePickerMonthYearInput"
    DATE_TIME_INPUT = "#dateAndTimePickerInput"


class DatePickerPage(BasePage):

    DATE_INPUT = "#datePickerMonthYearInput"
    DATE_TIME_INPUT = "#dateAndTimePickerInput"

    def open(self):
        # просто переход на страницу
        self.page.goto("https://demoqa.com/date-picker")

    def select_date(self, date_text):
        """
        date_text — строка вида "01 Jan 1990" или "01/01/1990"
        Ввод через fill() заменяет значение.
        """
        self.fill(self.DATE_INPUT, "")
        self.fill(self.DATE_INPUT, date_text)
        # иногда требуется нажать Enter
        self.page.keyboard.press("Enter")

    def select_date_time(self, datetime_text):
        # меняем значение в поле date & time
        self.fill(self.DATE_TIME_INPUT, "")
        self.fill(self.DATE_TIME_INPUT, datetime_text)
        self.page.keyboard.press("Enter")

    def get_selected_date(self):
        # получаем текущее значение date field
        return self.get_value(self.DATE_INPUT)

    def get_selected_date_time(self):
        # получаем значение date & time
        return self.get_value(self.DATE_TIME_INPUT)
