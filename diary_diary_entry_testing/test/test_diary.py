from lib.diary_2 import *
import pytest

"""
Given an empty Diary with no DiaryEntry objects
all() should return an empty list
"""
def test_no_diary_entries():
    d = Diary()
    assert d.all() == []

"""
Given an empty Diary with no DiaryEntry objects
Check count_words() method in Diary returns 0
"""
def test_count_words_no_diary_entries():
    d = Diary()
    assert d.count_words() == 0

"""
Given an empty Diary with no DiaryEntry objects
and a wpm greater than 0
Check reading_time() method in Diary returns 0
"""
def test_reading_time_no_diary_entries():
    d = Diary()
    assert d.reading_time(5) == "No entries to read."
"""
Given an empty Diary with no DiaryEntry objects
with a wpm of 5 and 2 minutes
Check if find_best_entry_for_reading_time() method returns "No entries to read."
"""

def test_find_best_entry_for_reading_time_no_diary_entries():
    d = Diary()
    assert d.find_best_entry_for_reading_time(5,2) == "No entries to read."

"""
Given an empty Diary with no DiaryEntry objects
and a wpm smaller or equal to 0
Check reading_time() method in Diary return an error message
"""
def test_reading_time_invalid_wpm():
    d = Diary()
    with pytest.raises(Exception) as err:
        d.reading_time(-1)
    error_message = str(err.value)
    assert error_message == "That is not a valid wpm."

"""
Given an empty Diary with no DiaryEntry objects
and a wpm/minutes smaller or equal to 0
Check find_best_entry_for_reading_time method in Diary return an error message
"""

def test_find_best_entry_for_reading_time_invalid_wpm_minutes():
    d = Diary()
    with pytest.raises(Exception) as err:
        d.find_best_entry_for_reading_time(1,-8)
    error_message = str(err.value)
    assert error_message == "You need valid wpm and minutes values."
