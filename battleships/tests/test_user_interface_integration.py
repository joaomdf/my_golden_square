import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game(), Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Player 1: Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("8")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("That is not a valid location.")
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("10")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".........S",
            ".........S",
            ".S.......S",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("10")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("That is not a valid location.")
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("10")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".........S",
            ".........S",
            ".S.......S",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            "SSSSS....."
        ]))
        io.expect_print("All your ships have been placed!")
        io.expect_print("Player 2: Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("8")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("That is not a valid location.")
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("10")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".........S",
            ".........S",
            ".S.......S",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("10")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("That is not a valid location.")
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("10")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".........S",
            ".........S",
            ".S.......S",
            ".S........",
            ".SSS......",
            "..........",
            "..........",
            "SSSS......",
            "..........",
            "SSSSS....."
        ]))
        io.expect_print("All your ships have been placed!")
        interface.run()