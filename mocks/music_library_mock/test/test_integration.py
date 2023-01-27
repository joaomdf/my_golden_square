from lib.music_library import *
from lib.track import *

"""
Given one Track object, track_1
Add it to the created music library
Check if list is updated to contain it
"""
def test_add_track_to_music_library():
    library = MusicLibrary()
    track_1 = Track("alright","kendrick lamar")
    library.add(track_1)
    assert library.track_list == [track_1]

"""
Given two Track objects, track_1 and track_2
Add them to the created music library
Check if list is updated to contain both
"""
def test_add_two_tracks_to_music_library():
    library = MusicLibrary()
    track_1 = Track("alright","kendrick lamar")
    library.add(track_1)
    track_2 = Track("don't stop me now", "queen")
    library.add(track_2)
    assert library.track_list == [track_1, track_2]

"""
Given two Track objects, track_1 and track_2, track_1 with the artist 'Kendrick Lamar', other with 'Drake'
Add them to the created music library
Given the keyword 'Kendrick Lamar' check is list returned from search returns list containing only track_1
"""
def test_add_two_tracks_to_music_library_and_return_one_match():
    library = MusicLibrary()
    track_1 = Track("alright","kendrick lamar")
    library.add(track_1)
    track_2 = Track("hotline bling", "drake")
    library.add(track_2)
    assert library.search("Kendrick Lamar") == [track_1]

"""
Given two Track objects, track_1 and track_2, both with artist 'Kendrick Lamar'
Add them to the created music library
Given the keyword 'Kendrick Lamar' check is list returns both Track objects
"""

"""
Given two Track objects, track_1 and track_2, track_1 with the artist 'Kendrick Lamar', other with 'Drake'
Add them to the created music library
Given the keyword 'Eminem' check is list returned from search is empty
"""