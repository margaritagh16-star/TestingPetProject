from pages.practice_form_page import PracticeFormPage

def test_fill_form(page):
    page.goto("https://demoqa.com/automation-practice-form")
    f = PracticeFormPage(page)
    f.enter_first_name("John")
    f.enter_last_name("Doe")
    f.enter_email("john@example.com")
    f.choose_gender("male")
    f.enter_mobile("1234567890")
    f.add_subject("Maths")
    f.check_hobby("sports")
    f.enter_address("123 Street")
    f.select_state("NCR")
    f.select_city("Delhi")
    f.submit()
    assert "John Doe" in f.get_result()
