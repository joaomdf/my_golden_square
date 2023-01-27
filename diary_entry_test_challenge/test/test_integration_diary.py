from lib.diary_3 import *
from lib.diary_entry_3 import *

"""
We want to check if it's sorting entries properly
"""

def test_all_diary_entries():
    entry_1 = DiaryEntry("Day 1", "I walked the dog today", "Diary Entry")
    entry_2 = DiaryEntry("Day 2", "I went skiing.", "Diary Entry")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all_diary_entries() == ["Day 1: I walked the dog today", "Day 2: I went skiing."]


def test_all_TODO_entries():
    entry_1 = DiaryEntry("Tomorrow", "Walk the dog", "TODO")
    entry_2 = DiaryEntry("Sometime this year", "Go skiing.", "TODO")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.todo_return() == ["Tomorrow: Walk the dog", "Sometime this year: Go skiing."]

def test_all_contact_entries():
    entry_1 = DiaryEntry("Mine", "07853345677", "Contact")
    entry_2 = DiaryEntry("Yours", "07853675677", "Contact")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.contacts_return() == ["Mine: 07853345677", "Yours: 07853675677"]

"""
check count_words returns
correct number of words in diary entries
"""

def test_entry_count_words():
    entry_1 = DiaryEntry("Day 1", "I walked the dog today", "Diary Entry")
    entry_2 = DiaryEntry("Day 2", "I went skiing.", "Diary Entry")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.best_entry_for_time(1,5) == "Day 2: I went skiing."

def test_entry_count_words_more_entries():
    entry_2 = DiaryEntry("Day 2", "Prosecutors said he was driven by an intense hatred for his country and angered by the flying of the Rainbow flag in support of the LGBT community. He was arrested in August 2021 and 800 euros of cash was found in his home in Potsdam.", "Diary Entry")
    entry_1 = DiaryEntry("Day 1", "I walked the dog today", "Diary Entry")
    entry_3 = DiaryEntry("Day 3", "Prosecutors alleged David Smith, 58, had wanted to hurt the UK and the embassy where he had worked for eight years. The Briton was accused of collecting intelligence about the embassy and leaking secret documents. Smith pleaded guilty at the Old Bailey to eight charges.", "Diary Entry")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.best_entry_for_time(5,10) == "Day 2: Prosecutors said he was driven by an intense hatred for his country and angered by the flying of the Rainbow flag in support of the LGBT community. He was arrested in August 2021 and 800 euros of cash was found in his home in Potsdam."