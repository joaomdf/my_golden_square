import string

class Track:
    def __init__(self, title, artist):
        if title == "" and artist == "":
            raise Exception("You must input an artist and title.")
        elif title == "":
            raise Exception("You must input a song title.")
        elif artist == "":
            raise Exception("You must input an artist.")
        self.title = string.capwords(title)
        self.artist = string.capwords(artist)

    def matches(self, keyword):
        return string.capwords(keyword) in self.title or string.capwords(keyword) in self.artist