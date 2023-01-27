'''
Recipe
---------
#1 Describe the problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

#2 Design the Class Interface
Class:
class MusicTracker:
there will an initializer but no parameter
ability to add a song to dictionary
display a list of songs that have been added

Methods:
- __init__() - no argument - used to assign empty dictionary, called music
- add_song() - two arguments - both strings, called artist and song - used to 
add artist + song concatenated string to music dictionary. It will default value to one if new 
dict record. otherwise it will increase the value by 1.
Side effect: updates dictionary with song list
- display_music() - no argument - used to return up to date dictionary with songs and times listened
'''

from lib.music_tracker import *
import pytest

'''
check if class displays empty dictionary
'''

def test_check_empty_dict():
    m = MusicTracker()
    assert m.display_music() == {}

'''
check if add a song to dictionary
song - don't stop me now
artist - queen
'''

def test_add_first_song_artist():
    m = MusicTracker()
    m.add_song("Queen", "Don't stop me now")
    assert m.display_music() == {"Queen - Don't stop me now": 1}

'''
check if can add 2 songs to dictionary and display updated dict
song - don't stop me now
artist - queen

song - all along the watchtower
artist - jimmi hendrix
'''

def test_add_three_songs():
    m = MusicTracker()
    m.add_song("Queen", "Don't stop me now")
    assert m.display_music() == {"Queen - Don't stop me now": 1}
    m.add_song("Jimmi Hendrix", "All along the watchtower")
    assert m.display_music() == {"Queen - Don't stop me now": 1, "Jimmi Hendrix - All along the watchtower": 1}
    m.add_song("Massive Attack", "Teardrop")
    assert m.display_music() == {"Queen - Don't stop me now": 1, "Jimmi Hendrix - All along the watchtower": 1, "Massive Attack - Teardrop": 1}
'''
check if can add 3 songs to dictionary but one of them is repeated

2x
song - don't stop me now
artist - queen

1x
song - all along the watchtower
artist - jimmi hendrix
'''
def test_add_repeat_song():
    m = MusicTracker()
    m.add_song("Queen", "Don't stop me now")
    assert m.display_music() == {"Queen - Don't stop me now": 1}
    m.add_song("Jimmi Hendrix", "All along the watchtower")
    assert m.display_music() == {"Queen - Don't stop me now": 1, "Jimmi Hendrix - All along the watchtower": 1}
    m.add_song("Queen", "Don't stop me now")
    m.add_song("Queen", "Don't stop me now")
    assert m.display_music() == {"Queen - Don't stop me now": 3, "Jimmi Hendrix - All along the watchtower": 1}


'''
check if the user has input both the artist and song name for add_song
artist = ""
song = all along the watchtower

'''

def test_check_input_both_add_song_arg():
    m = MusicTracker()
    with pytest.raises(Exception) as err:
        m.add_song("","All along the watchtower")
    error_message = str(err.value)
    assert error_message == "You must input both an artist and song title!"

def test_check_input_both_add_song_arg_existing_artist():
    m = MusicTracker()
    m.add_song("Queen", "Don't stop me now")
    with pytest.raises(Exception) as err:
        m.add_song("Queen","")
    error_message = str(err.value)
    assert error_message == "You must input both an artist and song title!"