import math

class Diary():
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        split_list = [word for entry in self._entries for word in entry.contents.split(" ")]
        return len(split_list)

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("That is not a valid wpm.")
        if self._entries == []:
            return "No entries to read."
        return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if wpm <= 0 or minutes <= 0:
            raise Exception("You need valid wpm and minutes values.")
        elif self.all() == []:
            return "No entries to read."
        else:
            total_words = wpm * minutes
            closest_number = 0
            chunk = None
            for entry in self._entries:
                if entry.count_words() <= total_words and entry.count_words() >= closest_number:
                    closest_number = entry.count_words()
                    chunk = entry
            return chunk

