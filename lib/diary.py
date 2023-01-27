import math

class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("You must have both a title and contents to read!")
        self.title = title
        self.contents = contents
        self.list_format = self.contents.split(" ")

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("You must enter a valid wpm!")
        else:
            return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        if wpm <= 0 or minutes <= 0:
            raise Exception("You must enter valid wpm and minutes!")
        else:
            total_words = wpm * minutes
            if len(self.list_format) <= total_words:
                chunk = " ".join(self.list_format)
                self.list_format = self.contents.split(" ")
                return chunk
            else:
                chunk = " ".join(self.list_format[0:total_words])
                self.list_format = self.list_format[total_words:]
                return chunk