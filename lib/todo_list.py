class ToDo():
    def __init__(self):
        self.list = []

    def add_todo(self, task):
        if task == "":
            raise Exception("That is not a valid task!")
        else:
            self.list.append(task)

    def check_todo(self):
        if self.list == []:
            return "Good job! You have no tasks to complete!"
        else:
            return self.list

    def update_todo(self, item):
        if self.list == []:
            raise Exception("You have no tasks left to complete!")
        else:
            if item not in range(len(self.list)):
                raise Exception("That is not a valid task!")
            else:
                del self.list[item]
                return "Good job, item has been removed from list!"