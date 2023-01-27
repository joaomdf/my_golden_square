---
Unit tests for Track

"""
Given a title 'Don't Stop me now' and artist 'Queen'
After creating an object with those strings
Check if new object exists by testing self.title and self.artist
"""

"""
Given an empty '' string title and an artist 'Kendrick Lamar'
Attempt to create an object with that string
Check if returns error message saying "You must input a song title"
"""

"""
Given an empty '' string artist and the title 'Poetic Justice'
Attempt to create an object with that string
Check if returns error message saying "You must input an artist"
"""

"""
Given empty '' strings for artist and title
Attempt to create an object with that string
Check if returns error message saying "You must input an artist and title"
"""

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Alright'
Check if method returns True
"""

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Godzilla'
Check if method returns False
"""

"""
Given a Track object with the title 'Alright' and artist 'Kendrick Lamar'
And a keyword 'Kendrick'
Check if method returns False
"""

"""
Given the title 'alright' and artist 'Kendrick Lamar'
Make sure self.title = 'Alright'
To guarantee user friendliness despite word case
"""

"""
Given the title 'Alright' and artist 'KENDRICK Lamar'
Make sure self.artist = 'Kendrick Lamar'
To guarantee user friendliness despite word case
"""

---
Unit tests for music_library

"""
Given an object for MusicLibrary with nothing added
Check if self.tracks return an empty list
"""

"""
Given an empty MusicLibrary
and calling search with any keyword
Check it returns message 'No tracks in library to search.'
"""

---
Integrations tests for music_library

"""
Given one Track object, track_1
Add it to the created music library
Check if list is updated to contain it
"""

"""
Given two Track objects, track_1 and track_2
Add them to the created music library
Check if list is updated to contain both
"""

"""
Given two Track objects, track_1 and track_2, track_1 with the artist 'Kendrick Lamar', other with 'Drake'
Add them to the created music library
Given the keyword 'Kendrick Lamar' check is list returned from search returns list containing only track_1
"""

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