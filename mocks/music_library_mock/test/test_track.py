from lib.track import *
import pytest

"""
Given a title 'Don't Stop me now' and artist 'Queen'
After creating an object with those strings
Check if new object exists by testing self.title and self.artist
"""
def test_object_is_created_with_title_and_artist():
    track_1 = Track("Don't stop me now", "Queen")
    assert track_1.title == "Don't Stop Me Now"
    assert track_1.artist == "Queen"

"""
Given an empty '' string title and an artist 'Kendrick Lamar'
Attempt to create an object with that string
Check if returns error message saying "You must input a song title"
"""
def test_failed_object_creation_empty_title():
    with pytest.raises(Exception) as err:
        Track("","Kendrick Lamar")
    error = str(err.value)
    assert error == "You must input a song title."

"""
Given an empty '' string artist and the title 'Poetic Justice'
Attempt to create an object with that string
Check if returns error message saying "You must input an artist"
"""
def test_failed_object_creation_empty_artist():
    with pytest.raises(Exception) as err:
        Track("Poetic Justice","")
    error = str(err.value)
    assert error == "You must input an artist."

"""
Given empty '' strings for artist and title
Attempt to create an object with that string
Check if returns error message saying "You must input an artist and title"
"""
def test_failed_object_creation_empty_artist_and_title():
    with pytest.raises(Exception) as err:
        Track("","")
    error = str(err.value)
    assert error == "You must input an artist and title."

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Alright'
Check if method returns True
"""
def test_matches_method_returns_true_for_match():
    track_1 = Track("Alright","Kendrick Lamar")
    assert track_1.matches("Alright") == True

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Godzilla'
Check if method returns False
"""
def test_matches_method_returns_false_for_no_match():
    track_1 = Track("Alright","Kendrick Lamar")
    assert track_1.matches("Godzilla") == False

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Kendrick'
Check if method returns False
"""
def test_matches_method_returns_true_for_partial_match():
    track_1 = Track("Alright","Kendrick Lamar")
    assert track_1.matches("Kendrick") == True

"""
Given the title 'alright' and artist 'Kendrick Lamar'
Make sure self.title = 'Alright'
To guarantee user friendliness despite word case
"""
def test_matches_method_returns_true_for_match_regardless_of_type_case_title():
    track_1 = Track("Alright","Kendrick Lamar")
    assert track_1.matches("alright") == True

"""
Given the title 'Alright' and artist 'KENDRICK Lamar'
Make sure self.artist = 'Kendrick Lamar'
To guarantee user friendliness despite word case
"""
def test_matches_method_returns_true_for_match_regardless_of_type_case_artist():
    track_1 = Track("Alright","Kendrick Lamar")
    assert track_1.matches("KENDRICK Lamar") == True