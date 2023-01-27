from lib.diary_entry import *
import pytest

"""
Given an object created with one or both arg being an empty string
Check if returns error message saying "That is not a valid entry, you need both a title and content."
"""
def test_class_instance_is_valid():
    with pytest.raises(Exception) as err:
        DiaryEntry("","It's a new year, and I'm super hungover.")
    error_message = str(err.value)
    assert error_message == "That is not a valid entry, you need both a title and content."

"""
Check if DiaryEntry can create instances of class
"1st January 2022" "It's a new year, and I'm super hungover."
"2nd January 2022" "New year's resolution, I'm never drinking again."
"3rd January 2022" "Water is life, water is love. The instruments of the devil shall not tempt me any longer."
"""
def test_check_objects_created():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    assert entry_1.title == "1st January 2022"
    assert entry_1.contents == "It's a new year, and I'm super hungover."
    entry_2 = DiaryEntry("2nd January 2022", "New year's resolution, I'm never drinking again.")
    assert entry_2.title == "2nd January 2022"
    assert entry_2.contents == "New year's resolution, I'm never drinking again."
    entry_3 = DiaryEntry("3rd January 2022", "Water is life, water is love. The instruments of the devil shall not tempt me any longer.")
    assert entry_3.title == "3rd January 2022"
    assert entry_3.contents == "Water is life, water is love. The instruments of the devil shall not tempt me any longer."

"""
Given an entry
Check if count_words() returns an integer with the right number of words
"""
def test_count_words_for_entry():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    assert entry_1.count_words() == 8
    entry_2 = DiaryEntry("2nd January 2022", "New year's resolution, I'm never drinking again.")
    assert entry_2.count_words() == 7

"""
Given an entry
check if reading_words() returns an estimate int of of count_words/wpm
"""
def test_reading_time_for_entry():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    assert entry_1.reading_time(2) == 4 
    entry_2 = DiaryEntry("2nd January 2022", "New year's resolution, I'm never drinking again.")
    assert entry_2.reading_time(5) == 2
    entry_3 = DiaryEntry("3rd January 2022", "Water is life, water is love. The instruments of the devil shall not tempt me any longer.")
    assert entry_3.reading_time(3) == 6

"""
Given an entry and a call with an invalid wpm
check if reading_words() returns "That's not a valid reading speed."
"""
def test_reading_words_if_invalid_wpm():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    with pytest.raises(Exception) as err:
        entry_1.reading_time(-3)
    error_message = str(err.value)
    assert error_message == "That is not a valid wpm."

"""
Given an entry 
check if reading_chunk() returns a string starting from tracker ending in wpm*minutes
"""
def test_reading_chunk_for_entry_including_continuation_and_restarts():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    assert entry_1.reading_chunk(3,1) == "It's a new"
    assert entry_1.reading_chunk(10,2) == "year, and I'm super hungover."
    assert entry_1.reading_chunk(10,2) == "It's a new year, and I'm super hungover."
    entry_2 = DiaryEntry("2nd January 2022", "New year's resolution, I'm never drinking again.")
    assert entry_2.reading_chunk(2,4) == "New year's resolution, I'm never drinking again."
    entry_3 = DiaryEntry("3rd January 2022", "Water is life, water is love. The instruments of the devil shall not tempt me any longer.")
    assert entry_3.reading_chunk(10,1) == "Water is life, water is love. The instruments of the"
    assert entry_3.reading_chunk(10,1) == "devil shall not tempt me any longer."
    assert entry_3.reading_chunk(10,1) == "Water is life, water is love. The instruments of the"

"""
Given an entry and a call with no valid wpm or minutes
check if reading_chunk() returns string "You need a valid reading speed and time."
"""
def test_reading_chunk_invalid_arg():
    entry_1 = DiaryEntry("1st January 2022", "It's a new year, and I'm super hungover.")
    with pytest.raises(Exception) as err:
        entry_1.reading_chunk(3,0)
    error_message = str(err.value)
    assert error_message == "You need a valid wpm and time."