from lib.string_builder import *

def test_adding_method():
    object = StringBuilder()
    object.add("I'm first!")
    result = object.output()
    assert result == "I'm first!"

def test_length_of_string():
    object = StringBuilder()
    object.add("I'm first!")
    result = object.size()
    assert result == 10

def test_length_with_no_addition():
    object = StringBuilder()
    result = object.size()
    assert result == 0

def test_adding_several():
    object = StringBuilder()
    object.add("I'm first!")
    object.add(" Well, I'm second, then!")
    object.add(" Whatever, I don't care about placements!")
    result = object.output()
    assert result == "I'm first! Well, I'm second, then! Whatever, I don't care about placements!"