Integration tests:

Will only occur for Diary class, since it relies on objects obtained from DiaryEntry but not vice versa

"""
Check add() method 
Adding three add() entries
all() sould return a list with both entries
"""

"""
Check count_words() method
Adding three add() entries
count_words() should return sum of count_words() method in each relevant DiaryEntry
"""

"""
Given three DiaryEntry records added
Check if reading_time() returns an estimate int of all entries
"""

------
Unit testing for Diary:

"""
Given an empty Diary with no DiaryEntry objects
all() should return an empty list
"""

"""
Given an empty Diary with no DiaryEntry objects
Check count_words() method in Diary returns 0
"""

"""
Given an empty Diary with no DiaryEntry objects
Check reading_time() method in Diary returns 0
"""

"""
Given an empty Diary with no DiaryEntry objects
Check if find_best_entry_for_reading_time() method returns "No entries to read."
"""

------
Unit testing for DiaryEntry

"""
Given an object created without both title and contents
Check if returns error message saying "You must add both a title and contents"
"""

"""
Given an entry
Check if count_words() returns an integer with the right number of words
"""

"""
Given an entry and a call with an invalid wpm
check if reading_words() returns "That's not a valid reading speed."
"""

"""
Given an entry
check if reading_words() returns an estimate int of of count_words/wpm
"""

"""
To copy from previous exercise
Given an entry and a call with no valid wpm or minutes
check if reading_chunk() returns string "You need a valid reading speed and time."
"""

"""
To copy from previous exercise
Given an entry 
check if reading_chunk() returns a string starting from tracker ending in wpm*minutes
"""