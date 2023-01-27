from lib.password_checker import *
import pytest

def test_password_is_eight_characters():
    x = PasswordChecker()
    assert x.check("qwertyui") == True

def test_password_is_more_than_eight_characters():
    x = PasswordChecker()
    assert x.check("qwertyuiop") == True

def test_password_is_invalid():
    x = PasswordChecker()
    with pytest.raises(Exception) as err:
        x.check("qwertyu")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."