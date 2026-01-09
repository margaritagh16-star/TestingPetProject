from pages.base_page import BasePage

class SelectMenuPage(BasePage):

    # стандартные селекты
    OLD_STYLE_SELECT = "#oldSelectMenu"

    # кастомные селекты с search
    MULTI_SELECT_INPUT = "#react-select-4-input"
    TITLE_SELECT_INPUT = "#react-select-3-input"
    STANDARD_MULTI_SELECT = "div[class*='multi-value__label']"

    # селект по цвету
    SELECT_VALUE_INPUT = "#react-select-2-input"
    SELECT_ONE_INPUT = "#react-select-3-input"
    SELECT_ONE_LABEL = "div[id*='selectOne'] .css-1uccc91-singleValue"
    SELECT_MULTI_LABELS = "div[class*='multi-value__label']"

    def open(self):
        self.page.goto("https://demoqa.com/select-menu")

    # ↓ *OLD STYLE* селект (тег <select>)
    def choose_old_style(self, value):
        self.select_option(self.OLD_STYLE_SELECT, value)

    def get_old_style_value(self):
        return self.page.locator(f"{self.OLD_STYLE_SELECT} option:checked").text_content()

    # ↓ типовые React-селекты

    def select_value(self, value):
        """
        Пример: "Red", "Blue", "Green"
        """
        self.fill(self.SELECT_VALUE_INPUT, value)
        self.page.keyboard.press("Enter")

    def get_selected_value(self):
        return self.get_text(self.SELECT_ONE_LABEL)

    def select_one(self, text):
        self.fill(self.SELECT_ONE_INPUT, text)
        self.page.keyboard.press("Enter")

    def get_selected_one(self):
        return self.get_text(self.SELECT_ONE_LABEL)

    def select_multi(self, values: list[str]):
        """
        Пример: ["Red", "Blue"]
        """
        for v in values:
            self.fill(self.MULTI_SELECT_INPUT, v)
            self.page.keyboard.press("Enter")

    def get_selected_multi(self):
        """
        Вернёт список выбранных значений
        """
        labels = self.page.locator(self.STANDARD_MULTI_SELECT).all_text_contents()
        return labels
