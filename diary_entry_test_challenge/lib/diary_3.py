class Diary:
    def __init__(self):
        self.all_diary_list = []
        self.todo_list = []
        self.contact_list = []

    def add(self, entry):
        if entry.type == "DIARY ENTRY":
            self.all_diary_list.append(entry)
        elif entry.type == "TODO":
            self.todo_list.append(entry)
        elif entry.type == "CONTACT":
            self.contact_list.append(entry)
    
    def all_diary_entries(self):
        return [entry.formatted_entry for entry in self.all_diary_list]

    def best_entry_for_time(self, wpm, time):
        total_words = wpm * time
        best_entry_number_of_words = 0
        best_entry = ""
        for entry in self.all_diary_list:
            if len(entry.formatted_entry.split(" ")) <= total_words and len(entry.formatted_entry.split(" ")) > best_entry_number_of_words:
                best_entry_number_of_words = len(entry.formatted_entry.split(" "))
                best_entry = entry.formatted_entry
        return best_entry

    def todo_return(self):
        return [entry.formatted_entry for entry in self.todo_list]

    def contacts_return(self):
        return [entry.formatted_entry for entry in self.contact_list]
