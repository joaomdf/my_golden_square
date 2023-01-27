from lib.diary import *

"""
Creates a diary record
"""
def test_diary_record():
    d = Diary("This is my entrance to my diary")
    assert d != None