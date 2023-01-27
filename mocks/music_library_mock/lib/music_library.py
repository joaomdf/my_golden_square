import string

class MusicLibrary:

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        if self.track_list == []:
            return "No tracks in library to search."
        else:
            s = [x for x in self.track_list if x.matches(string.capwords(keyword)) == True]
            return s