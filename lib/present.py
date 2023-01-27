class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A present has already been wrapped!")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No present has been wrapped!")
        return self.contents