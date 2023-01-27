from lib.report_length import *

def test_length_normal():
    length = report_length("Hello, I am a string.")
    assert length == "This string was 21 characters long."

def test_length_empty_string():
    length = report_length("")
    assert length == "This string was 0 characters long."

def test_length_not_string():
    length = report_length(5)
    assert length == "This is not a string!"