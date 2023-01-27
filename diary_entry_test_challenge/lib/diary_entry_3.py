import re 

class DiaryEntry:
    def __init__(self, title, contents, type):
        self.title = title.strip()
        self.contents = contents.strip()
        self.type = type.upper()
        if self.title == "":
            raise Exception("You need to enter a title!")
        if self.contents == "":
            raise Exception("You need to enter valid contents!")
        if self.type == "DIARY ENTRY" or self.type == "TODO" or self.type == "CONTACT":
            if self.type == "CONTACT":
                if re.findall(r"0[0-9]{10}",self.contents):
                    self.formatted_entry = f"{title}: {contents}"
                else:
                    raise Exception("Phone number is invalid!")
            self.formatted_entry = f"{title}: {contents}"
        else:
            raise Exception("That is an invalid entry type! Please use Diary Entry, TODO or Contact.")
