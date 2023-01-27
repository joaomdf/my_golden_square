from lib.diary_2 import *
from lib.diary_entry import *
"""
Given a Diary object with several DiaryEntry instances
"1st January 2022" "It's a new year, and I'm super hungover."
"2nd January 2022" "New year's resolution, I'm never drinking again."
"3rd January 2022" "Water is life, water is love. The instruments of the devil shall not tempt me any longer."
Test all methods operate as expected
add(), all(), count_words(), reading_time(), find_best_entry_for_reading_time
"""

def test_integrated_testing_methods():
    d = Diary()
    entry_1 = DiaryEntry("1st January 2022", "New year's resolution, I'm never drinking again.")
    d.add(entry_1)
    assert d.all() == [entry_1]
    entry_2 = DiaryEntry("2nd January 2022", "It's a new year, and I'm super hungover.")
    d.add(entry_2)
    assert d.all() == [entry_1, entry_2]
    entry_3 = DiaryEntry("3rd January 2022", "Water is life, water is love. The instruments of the devil shall not tempt me any longer.")
    d.add(entry_3)
    assert d.all() == [entry_1, entry_2, entry_3]
    assert d.count_words() == 32
    
    assert d.reading_time(3) == 11
    assert d.find_best_entry_for_reading_time(6,3) == entry_3
    assert d.find_best_entry_for_reading_time(4,2) == entry_2
    assert d.find_best_entry_for_reading_time(1,2) == None