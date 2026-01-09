class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_value(self, locator):
        return self.page.locator(locator).input_value()

    def select_option(self, locator, value):
        self.page.locator(locator).select_option(value)

    def switch_to_window(self, index):
        pages = self.page.context.pages
        self.page = pages[index]
        return self.page

    def handle_dialog(self, accept=True, prompt_text=None):
        """
        Регистрация обработчика диалога перед действием.
        accept=True — нажимает OK,
        accept=False — нажимает Cancel (если применимо),
        prompt_text — ввод текста в prompt-диалог.
        """
        def dialog_handler(dialog):
            if prompt_text is not None:
                dialog.accept(prompt_text)
            elif accept:
                dialog.accept()
            else:
                dialog.dismiss()
        self.page.once("dialog", dialog_handler)