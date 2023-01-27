from lib.music_library import *
from unittest.mock import Mock

#Before mock testing

"""
Given an object for MusicLibrary with nothing added
Check if self.tracks return an empty list
"""
def test_check_empty_track_list():
    library = MusicLibrary()
    assert library.track_list == []

"""
Given an empty MusicLibrary
and calling search with any keyword
Check it returns message 'No tracks in library to search.'
"""
def test_check_message_for_search_if_library_is_empty():
    library = MusicLibrary()
    assert library.search("alright") == "No tracks in library to search."

#With mock testing

"""
Given one Track object, track_1
Add it to the created music library
Check if list is updated to contain it
"""
def test_mock_adding_track_to_library():
    library = MusicLibrary()
    fake_track_entry = Mock()
    library.add(fake_track_entry)
    assert library.track_list == [fake_track_entry]

"""
Given two Track objects, track_1 and track_2
Add them to the created music library
Check if list is updated to contain both
"""
def test_mock_adding_two_track_to_library():
    library = MusicLibrary()
    fake_track_entry_1 = Mock()
    fake_track_entry_2 = Mock()
    library.add(fake_track_entry_1)
    library.add(fake_track_entry_2)
    assert library.track_list == [fake_track_entry_1, fake_track_entry_2]

"""
Given two Track objects, track_1 and track_2, track_1 with the artist 'Kendrick Lamar', other with 'Drake'
Add them to the created music library
Given the keyword 'Kendrick Lamar' check is list returned from search returns list containing only track_1
"""
def test_mock_search_one_match():
    library = MusicLibrary()
    fake_track_entry_1 = Mock()
    fake_track_entry_1.matches.return_value = True
    fake_track_entry_2 = Mock()
    fake_track_entry_2.matches.return_value = False
    library.add(fake_track_entry_1)
    library.add(fake_track_entry_2)
    assert library.search("Kendrick Lamar") == [fake_track_entry_1]

"""
Given two Track objects, track_1 and track_2, both with artist 'Kendrick Lamar'
Add them to the created music library
Given the keyword 'Kendrick Lamar' check is list returns both Track objects
"""
def test_mock_search_two_matches():
    library = MusicLibrary()
    fake_track_entry_1 = Mock()
    fake_track_entry_1.matches.return_value = True
    fake_track_entry_2 = Mock()
    fake_track_entry_2.matches.return_value = True
    library.add(fake_track_entry_1)
    library.add(fake_track_entry_2)
    assert library.search("Kendrick Lamar") == [fake_track_entry_1, fake_track_entry_2]

"""
Given two Track objects, track_1 and track_2, track_1 with the artist 'Kendrick Lamar', other with 'Drake'
Add them to the created music library
Given the keyword 'Eminem' check is list returned from search is empty
"""
def test_mock_search_no_matches():
    library = MusicLibrary()
    fake_track_entry_1 = Mock()
    fake_track_entry_1.matches.return_value = False
    fake_track_entry_2 = Mock()
    fake_track_entry_2.matches.return_value = False
    library.add(fake_track_entry_1)
    library.add(fake_track_entry_2)
    assert library.search("Eminem") == []