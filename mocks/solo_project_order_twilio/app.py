from lib.order import *
import re

class Application():
    def __init__(self):
        self.new_order = Order()
        self.text = "Y"

    def run(self):
        print("Welcome to this gig economy nightmare! Here's the menu!")
        print(self.new_order.check_menu())
        choices = input("Please select the your item choices.")
        while (self.text == "Y"):
            self.new_order.add_item(choices)
            self.text = input("Do you have more items to add? (Y/N)").capitalize()
            if self.text != "Y":
                print("That is not a valid option!")
        print("Here's your order invoice!")
        self.new_order.check_receipt()
        self.text = input("Please input your phone number for order updates.")
        while (not re.fullmatch(r"^0\d{10}$", self.text)):
            self.text = input("That is not a valid number. Please try again!")
        self.new_order.confirmed_text(f"+44{self.text}")



if __name__ == '__main__':
    app = Application()
    app.run()