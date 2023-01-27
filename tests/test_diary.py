from lib.diary import *
import pytest 

def test_format():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    assert d.format() == "My diary: Dear Diary, today i did some coding..."

def test_count_words():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    assert d.count_words() == 7

def test_count_words_no_title_or_content():
    with pytest.raises(Exception) as err:
        d = DiaryEntry("My diary", "")
    error_message = str(err.value)
    assert error_message == "You must have both a title and contents to read!"

def test_reading_time():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    assert d.reading_time(70) == 1

def test_small_reading_chunk():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    assert d.reading_chunk(5,2) == "Dear Diary, today i did some coding..."

def test_large_reading_chunk():
    d = DiaryEntry("My diary", "Blessed be God, at the end of the last year I was in very good health, without any sense of my old pain, but upon taking of cold. I lived in Axe Yard having my wife, and servant Jane, and no more in family than us three. My wife … gave me hopes of her being with child, but on the last day of the year … [the hope was belied.]2 The condition of the State was thus; viz. the Rump, after being disturbed by my Lord Lambert, was lately returned to sit again. The officers of the Army all forced to yield. Lawson lies still in the river, and Monk is with his army in Scotland. Only my Lord Lambert is not yet come into the Parliament, nor is it expected that he will without being forced to it. The new Common Council of the City do speak very high; and had sent to Monk their sword-bearer, to acquaint him with their desires for a free and full Parliament, which is at present the desires, and the hopes, and expectation of all. Twenty-two of the old secluded members3 having been at the House-door the last week to demand entrance, but it was denied them; and it is believed that [neither] they nor the people will be satisfied till the House be filled. My own private condition very handsome, and esteemed rich, but indeed very poor; besides my goods of my house, and my office, which at present is somewhat uncertain. Mr. Downing master of my office. (Lord’s Day) This morning (we living lately in the garret) I rose, put on my suit with great skirts, having not lately worn any other, clothes but them. Went to Mr. Gunning’s chapel at Exeter House, where he made a very good sermon upon these words: — “That in the fulness of time God sent his Son, made of a woman,” &c.; showing, that, by “made under the law,” is meant his circumcision, which is solemnized this day.")
    assert d.reading_chunk(5,2) == "Blessed be God, at the end of the last year"

def test_several_reading_chunk():
    d = DiaryEntry("My diary", "Blessed be God, at the end of the last year I was in very good health, without any sense of my old pain, but upon taking of cold. I lived in Axe Yard having my wife, and servant Jane, and no more in family than us three. My wife … gave me hopes of her being with child, but on the last day of the year … [the hope was belied.]2 The condition of the State was thus; viz. the Rump, after being disturbed by my Lord Lambert, was lately returned to sit again. The officers of the Army all forced to yield. Lawson lies still in the river, and Monk is with his army in Scotland. Only my Lord Lambert is not yet come into the Parliament, nor is it expected that he will without being forced to it. The new Common Council of the City do speak very high; and had sent to Monk their sword-bearer, to acquaint him with their desires for a free and full Parliament, which is at present the desires, and the hopes, and expectation of all. Twenty-two of the old secluded members3 having been at the House-door the last week to demand entrance, but it was denied them; and it is believed that [neither] they nor the people will be satisfied till the House be filled. My own private condition very handsome, and esteemed rich, but indeed very poor; besides my goods of my house, and my office, which at present is somewhat uncertain. Mr. Downing master of my office. (Lord’s Day) This morning (we living lately in the garret) I rose, put on my suit with great skirts, having not lately worn any other, clothes but them. Went to Mr. Gunning’s chapel at Exeter House, where he made a very good sermon upon these words: — “That in the fulness of time God sent his Son, made of a woman,” &c.; showing, that, by “made under the law,” is meant his circumcision, which is solemnized this day.")
    first = d.reading_chunk(5,2)
    second = d.reading_chunk(5,2)
    assert second == "I was in very good health, without any sense of"

def test_return_to_start():
    d = DiaryEntry("My diary", "Blessed be God, at the end of the last year I was in very good health, without any sense of my old pain.")
    first = d.reading_chunk(5,2)
    second = d.reading_chunk(5,2)
    third = d.reading_chunk(6,2)
    forth = d.reading_chunk(6,2)
    assert first == "Blessed be God, at the end of the last year"
    assert second == "I was in very good health, without any sense of"
    assert third == "my old pain."
    assert forth == "Blessed be God, at the end of the last year I was"

def test_reading_time_given_wpm_equal_0():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    with pytest.raises(Exception) as err:
        d.reading_time(0)
    error_message = str(err.value)
    assert error_message == "You must enter a valid wpm!"

def test_reading_chunk_given_invalid_wpm_or_min():
    d = DiaryEntry("My diary", "Dear Diary, today i did some coding...")
    with pytest.raises(Exception) as err:
        d.reading_chunk(0,0)
    error_message = str(err.value)
    assert error_message == "You must enter valid wpm and minutes!"