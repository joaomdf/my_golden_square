class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.points_to_check = []
        

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"

    def valid(self):
        if self.col < 0 or self.col > 9 or self.row < 0 or self.row > 9:
            return False
        if self.orientation == "vertical":
            return self.row + self.length <= 9
        else:
            return self.col + self.length <= 9
    
    def update_points_to_check(self):
        if self.orientation == "vertical":
            for i in range(self.row, self.row + self.length):
                self.points_to_check.append([i,self.col])
        else:
            for i in range(self.col, self.col + self.length):
                self.points_to_check.append([self.row, i])