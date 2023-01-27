import re
from twilio.rest import Client
from datetime import datetime, timedelta

class Order:
    def __init__(self):
        self.order = []
        self.menu = {
            "Hunter's Chicken": {"Menu number": "1", "Price": "£9.79"},
            "All Day Breakfast": {"Menu number": "2", "Price": "£9.99"},
            "Farmhouse Chicken Tikka Masala": {"Menu number": "3", "Price": "£10.79"},
            "Crispy Chicken Medley": {"Menu number": "4", "Price": "£9.79"},
            "Beef Lasagne": {"Menu number": "5", "Price": "£9.79"},
            "Luxury Macaroni Cheese": {"Menu number": "6", "Price": "£7.49"},
            "Smothered Chicken": {"Menu number": "7", "Price": "£9.79"},
            "Curried Chicken Skewer": {"Menu number": "8", "Price": "£9.49"},
            "Tuna Melt Sandwich": {"Menu number": "9", "Price": "£5.99"},
            "Carvery": {"Menu number": "10", "Price": "£11.50"}
            }

    def check_menu(self):
        menu = "Menu:"
        count = 1
        while count <= len(self.menu):
            for key in self.menu.keys():
                if int(self.menu[key]["Menu number"]) == count:
                    menu += "\n" + self.menu[key]["Menu number"] + ". " + key + ": " + self.menu[key]["Price"]
                    count += 1
        return menu

    def add_item(self, item):
        requests = re.split(r'\D+', item)
        menu_numbers = [value["Menu number"] for key, value in self.menu.items()]
        for i in requests:
            if i not in menu_numbers:
                raise Exception("That is not a valid option.")
        for i in requests:
            for key in self.menu.keys():
                if self.menu[key]["Menu number"] == i:
                    self.order.append(key)

    def check_receipt(self):
        if self.order == []:
            raise Exception ("This bitch is empty. Yeet!")
        string = "Your order:"
        price = 0
        for item in self.order:
            string += "\n" + item + ": " + self.menu[item]["Price"]
            price += float(self.menu[item]["Price"][1:])
        string += "\nGrand Total: £" + '%.2f' % price
        return string

    def confirmed_text(self, phone_number):
        client = Client(###################, #######################)
        delivery_time = (datetime.now() + timedelta(hours=1)).strftime("%H:%M")
        message = client.messages.create(
            to=phone_number, 
            from_=################,
            body=f"Thank you! Your order was placed and will be delivered before {delivery_time}"
            )
        return message.sid