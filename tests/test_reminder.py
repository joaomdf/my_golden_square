from lib.reminder import *
import pytest

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    assert reminder.remind() == "Walk the dog, Kay!"

def test_reminder_error():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"