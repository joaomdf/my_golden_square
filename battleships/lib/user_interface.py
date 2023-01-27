class UserInterface:
    def __init__(self, io, player_one, player_two):
        self.io = io
        self.player_one = player_one
        self.player_two = player_two
        self.list_players = [self.player_one, self.player_two]
        self.current_player = player_one
        self.next_player = player_two

    def run(self):
        self._show("Welcome to the game!")
        for player in self.list_players:
            self._show("Player {}: Set up your ships first.".format(self.list_players.index(player) + 1))
            while len(player.unplaced_ships()) > 0:
                current_state = len(player.ships_placed)
                self._show("You have these ships remaining: {}".format(
                    self._ships_unplaced_message(player)))
                self._prompt_for_ship_placement(player)
                if len(player.ships_placed) == current_state:
                    self._show("That is not a valid location.")
                else:
                    self._show("This is your board now:")
                    self._show(self._format_board(player))
            self._show("All your ships have been placed!")
        self._match()

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self, player):
        ship_lengths = [str(ship.length) for ship in player.unplaced_ships()]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self, player):        
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        player.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )
        self._show("OK.")

    def _format_board(self, player):
        rows = []
        for row in range(1, player.rows + 1):
            row_cells = []
            for col in range(1, player.cols + 1):
                if player.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)

    def _prompt_for_hit(self, player):
        hit = self._prompt("Player {}, what are your attack coordinates? (row/column)".format(self.list_players.index(player) + 1))
        coordinates = hit.split("/")
        coordinates_number = [int(x) for x in coordinates]
        return coordinates_number

    def _match(self):
        while self.current_player.
        coordinates = self._prompt_for_hit(self.current_player)
        self.current_player.hit(self.next_player.board_for_enemy, coordinates[0], coordinates[1])
        self._format_enemy_board(self.next_player)

    def _format_enemy_board(self, player):
        formatted = ""
        for row in player.board:
            new_row = "".join(row)
            new_row += "\n"
            formatted += new_row
        return formatted
