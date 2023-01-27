from lib.ship import Ship
from lib.ship_placement import ShipPlacement

class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.ships_not_placed = [Ship(2), Ship(3), Ship(3), Ship(4),Ship(5)]
        self.rows = rows
        self.cols = cols
        self.board = [["." for i in range(cols)] for j in range(rows)]
        self.board_for_enemy = [["." for i in range(cols)] for j in range(rows)]

    def unplaced_ships(self):
        return self.ships_not_placed

    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row-1,
            col=col-1,
        )
        if ship_placement.valid() == False:
            return
        else:
            ship_placement.update_points_to_check()
            for point in ship_placement.points_to_check:
                if self.board[point[0]][point[1]] == "S":
                    return
            for point in ship_placement.points_to_check:
                self.board[point[0]][point[1]] = "S"
            self.ships_placed.append(ship_placement)
            for ship in self.ships_not_placed:
                if ship.length == length:
                    self.ships_not_placed.remove(ship)
                    return

    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row-1, col-1):
                return True
        return False

    def hit(self, enemy_board, row, col):
        if enemy_board[row - 1][col - 1] == "S":
            self.board_for_enemy[row - 1][col - 1] = "H"
        elif enemy_board[row - 1][col - 1] == ".":
            self.board_for_enemy[row - 1][col - 1] = "M"
