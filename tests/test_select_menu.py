import pytest


from pages.select_menu_page import SelectMenuPage

def test_old_style_select(page):
    select_menu = SelectMenuPage(page)
    select_menu.open()

    select_menu.choose_old_style("Red")
    assert select_menu.get_old_style_value() == "Red"

def test_select_value(page):
    select_menu = SelectMenuPage(page)
    select_menu.open()

    select_menu.select_value("Green")
    assert select_menu.get_selected_value() == "Green"

def test_select_one(page):
    select_menu = SelectMenuPage(page)
    select_menu.open()

    select_menu.select_one("Group 1, option 2")
    assert select_menu.get_selected_one() == "Group 1, option 2"

def test_select_multi(page):
    select_menu = SelectMenuPage(page)
    select_menu.open()

    select_menu.select_multi(["Red", "Blue", "Green"])
    selected = select_menu.get_selected_multi()
    assert sorted(selected) == sorted(["Red", "Blue", "Green"])
