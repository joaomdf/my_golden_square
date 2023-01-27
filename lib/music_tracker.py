class MusicTracker:
    def __init__(self):
        self._music = {}
    
    def add_song(self, artist, song):
        if artist == "" or song == "":
            raise Exception("You must input both an artist and song title!")
        record = artist + " - " + song
        if self._music.get(record) != None:
            self._music[record] += 1
        else:
            self._music[record] = 1

    def display_music(self):
        return self._music