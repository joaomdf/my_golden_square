from lib.diary_3 import *

"""
check returns for empty lists
"""

def test_diary_list():
    diary = Diary()
    assert diary.all_diary_entries() == []

def test_contact_list():
    diary = Diary()
    assert diary.contacts_return() == []

def test_todo_list():
    diary = Diary()
    assert diary.todo_return() == []