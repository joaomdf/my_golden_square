As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

#With twilio-python and mocks

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


Menu will be:
menu = {
    "Hunter's Chicken": {"Menu number": "1", "Price": "£9.79"},
    "All Day Breakfast": {"Menu number": "2", "Price": "£9.99"},
    "Farmhouse Chicken Tikka Masala": {"Menu number": "3", "Price": "£10.79"},
    "Crispy Chicken Medley": {"Menu number": "4", "Price": "£9.79"},
    "Beef Lasagne": {"Menu number": "5", "Price": "££9.79"},
    "Luxury Macaroni Cheese": {"Menu number": "6", "Price": "£7.49"},
    "Smothered Chicken": {"Menu number": "7", "Price": "£9.79"},
    "Curried Chicken Skewer": {"Menu number": "8", "Price": "£9.49"},
    "Tuna Melt Sandwich": {"Menu number": "9", "Price": "£5.99"},
    "Carvery": {"Menu number": "10", "Price": "£11.50"}
}

Order class

import twillio

Contains methods
__init__ - Will create menu list of tuples with all items available for order
         - Will create an empty order_items list

check_menu - will not use any arguments
           - returns the list of tuples with menu

add_item - will have a string with numbers as argument - these numbers are the items to be added
         - can add one or several items at once
         - side effect - updates chosen items list

check_receipt - will have no arguments
              - returns order_items list

confirmed_text - will have no arguments
           - should check current time and use twillio to send text with string "Your order has been confirmed. It should arrive at {current_time + 1}"

"""
Check if class instance creates menu 
Check if class instance creates empty order_list
"""

"""
Check if check_menu returns the menu
"""

"""
Check if add_item will update order_items
"""

"""
Check if add_item raises error exception if not listed item is chosen
"""

"""
Check if after adding items to order_list check_receipt returns a list of items as well as the total price
"""

"""
Check if check_receipt raises error exception if not items have been added to order
"""

"""
Check if order text somthing something
"""



