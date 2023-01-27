import sys
from lib.game import Game
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()
player_one = Game()
player_two = Game()
user_interface = UserInterface(io, player_one, player_two)
user_interface.run()
