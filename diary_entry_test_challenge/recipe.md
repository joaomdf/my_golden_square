1st story:
records of experiences
kept in diary => list or dictionary

2nd story:
returns the experiences kept in diary

3rd story:
access specific entries based on time they have to read

4th story:
list of tasks

5th story:
access list and identify and record phone numbers



Class Diary
__init__ - contain self._entries_list as list 
         - self._contacts_list as dict
         - self._todo_list

add - one arg - object from DiaryEntry
no return

all_diary_entries() - no argument
returns list of diary entries

diary_entry_count_words() - no argument
creates list of word count for each self._entries_list

best_entry_for_time() - two arguments - wpm and time (both integers)
return best diary entry for wpm*time

all_todo_return - no argument
returns list of TODO tasks

all_contacts_return - no argument
returns list of contacts

class DiaryEntries
__init__ - title and contents and type
only accepts 3 types of titles - TODO, Phone Number and Diary Entry