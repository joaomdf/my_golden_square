from lib.diary_entry_3 import *
import pytest

"""
Given a correct input 
Check that formatting works
"""
def test_correct_formatting_diary_entry():
    entry_1 = DiaryEntry("Day 1", "I walked the dog today.", "diary entry")
    assert entry_1.formatted_entry == "Day 1: I walked the dog today."

def test_correct_formatting_contact():
    entry_2 = DiaryEntry("Mine", "07853345677", "Contact")
    assert entry_2.formatted_entry == "Mine: 07853345677"

def test_correct_formatting_todo():
    entry_3 = DiaryEntry("Sometime this year", "Go skiing.", "toDo")
    assert entry_3.formatted_entry == "Sometime this year: Go skiing."
"""
Given the wrong type
return "That is not a valid type of entry!"
"""
def test_invalid_entry_type():
    with pytest.raises(Exception) as err:
        diary_entry = DiaryEntry("Day 1", "Walked the house", "Whale")
    error = str(err.value)
    assert error == "That is an invalid entry type! Please use Diary Entry, TODO or Contact."


"""
Given a correct type "Contact" and an invalid number
Raise error "That is not a valid phone number!"
"""
def test_invalid_contact():
    with pytest.raises(Exception) as err:
        entry_1 = DiaryEntry("Mine", "078533456", "Contact")
    error = str(err.value)
    assert error == "Phone number is invalid!"

"""
Make sure contents and title are never passed as empty string
"""

def test_empty_title():
    with pytest.raises(Exception) as err:
        entry_1 = DiaryEntry("    ", "go for a walk", "TODo")
    error = str(err.value)
    assert error == "You need to enter a title!"

def test_empty_contents():
    with pytest.raises(Exception) as err:
        entry_1 = DiaryEntry("Day 1", "    ", "TODo")
    error = str(err.value)
    assert error == "You need to enter valid contents!"