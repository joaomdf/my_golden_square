from lib.gratitudes import *

def test_return_without_adding_gratitudes():
    object = Gratitudes()
    assert object.format() == "Be grateful for: "

def test_return_with_one_gratitude():
    object = Gratitudes()
    object.add("Family")
    assert object.format() == "Be grateful for: Family"

def test_return_with_two_added_gratitudes():
    object = Gratitudes()
    object.add("Family")
    object.add("Friends")
    assert object.format() == "Be grateful for: Family, Friends"