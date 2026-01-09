from pages.base_page import BasePage

class PracticeFormPage(BasePage):

    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    EMAIL = "#userEmail"
    GENDER_MALE = "label[for='gender-radio-1']"
    GENDER_FEMALE = "label[for='gender-radio-2']"
    GENDER_OTHER = "label[for='gender-radio-3']"
    MOBILE = "#userNumber"
    DOB_INPUT = "#dateOfBirthInput"
    SUBJECTS_INPUT = "#subjectsInput"
    HOBBIES_SPORTS = "label[for='hobbies-checkbox-1']"
    HOBBIES_READING = "label[for='hobbies-checkbox-2']"
    HOBBIES_MUSIC = "label[for='hobbies-checkbox-3']"
    CURRENT_ADDRESS = "#currentAddress"
    STATE_INPUT = "#react-select-3-input"
    CITY_INPUT = "#react-select-4-input"
    SUBMIT = "#submit"
    RESULT_TABLE = ".modal-content"

    def enter_first_name(self, name):
        self.fill(self.FIRST_NAME, name)

    def enter_last_name(self, name):
        self.fill(self.LAST_NAME, name)

    def enter_email(self, email):
        self.fill(self.EMAIL, email)

    def choose_gender(self, gender):
        locator = {
            "male": self.GENDER_MALE,
            "female": self.GENDER_FEMALE,
            "other": self.GENDER_OTHER
        }
        self.click(locator.get(gender.lower()))

    def enter_mobile(self, phone):
        self.fill(self.MOBILE, phone)

    def enter_dob(self, date_str):
        self.fill(self.DOB_INPUT, date_str)

    def add_subject(self, subject):
        self.fill(self.SUBJECTS_INPUT, subject)
        self.page.keyboard.press("Enter")

    def check_hobby(self, hobby):
        locator = {
            "sports": self.HOBBIES_SPORTS,
            "reading": self.HOBBIES_READING,
            "music": self.HOBBIES_MUSIC
        }
        self.click(locator.get(hobby.lower()))

    def enter_address(self, address):
        self.fill(self.CURRENT_ADDRESS, address)

    def select_state(self, state):
        self.fill(self.STATE_INPUT, state)
        self.page.keyboard.press("Enter")

    def select_city(self, city):
        self.fill(self.CITY_INPUT, city)
        self.page.keyboard.press("Enter")

    def submit(self):
        self.click(self.SUBMIT)

    def get_result(self):
        return self.get_text(self.RESULT_TABLE)
