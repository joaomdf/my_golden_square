import math

class DiaryEntry():

    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("That is not a valid entry, you need both a title and content.")
        self.title = title
        self.contents = contents
        self.tracker = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("That is not a valid wpm.")
        return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        if wpm <=0 or minutes <= 0:
            raise Exception("You need a valid wpm and time.")
        total_words = wpm * minutes
        listed_contents = self.contents.split(" ")
        chunk = " ".join(listed_contents[self.tracker:self.tracker + total_words])
        if self.tracker  + total_words >= self.count_words():
            self.tracker = 0
        else:
            self.tracker += total_words
        return chunk