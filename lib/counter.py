class Counter:
    def __init__(self):
        self.count = 0
        self.current = 0
    
    def add(self, num):
        self.current = self.count
        self.count += num

    def report(self):
        if self.current == self.count:
            return f"You have not counted!"
        else:
            return f"Counted to {self.count} so far."