from lib.secret_diary import *
from lib.diary import *
"""
Given an instance of diary,
create an unlocked instance of secret_diary
"""
def test_create_secret_diary_record():
    d = Diary("This is my entrance to my diary")
    s = SecretDiary(d)
    assert s != None

"""
Given an instance of diary used to create an instance of secret_diary
check if it can be read
"""
def test_read