from lib.present import *
import pytest

def test_unwrapping_nothing():
    x = Present()
    with pytest.raises(Exception) as e:
        x.unwrap()
    error_message = str(e.value)
    assert error_message == "No present has been wrapped!"

def test_wrapping_present():
    x = Present()
    x.wrap("Pair of socks")
    assert x.contents == "Pair of socks"

def test_wrapping_several_presents():
    x = Present()
    x.wrap("Pair of socks")
    with pytest.raises(Exception) as e:
        x.wrap("Bottle of wine")
    error_message = str(e.value)
    assert error_message == "A present has already been wrapped!"
