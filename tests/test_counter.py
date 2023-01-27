from lib.counter import *

def test_count_to_10():
    count = Counter()
    count.add(10)
    assert count.report() == "Counted to 10 so far."


def test_count_to_20_with_two_adds():
    count = Counter()
    count.add(10)
    count.add(10)
    assert count.report() == "Counted to 20 so far."


def test_have_not_counted():
    count = Counter()
    count.add(0)
    assert count.report() == "You have not counted!"