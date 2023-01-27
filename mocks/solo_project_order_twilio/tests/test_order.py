from unittest import mock
from lib.order import *
import pytest

# """
# Check if class instance creates menu 
# Check if class instance creates empty order_list
# """

# def test_initialiser_creates_menu_and_empty_order():
#     my_order = Order()
#     assert my_order.order == []
#     assert my_order.menu == {"Hunter's Chicken": {"Menu number": "1", "Price": "£9.79"}, "All Day Breakfast": {"Menu number": "2", "Price": "£9.99"}, "Farmhouse Chicken Tikka Masala": {"Menu number": "3", "Price": "£10.79"}, "Crispy Chicken Medley": {"Menu number": "4", "Price": "£9.79"}, "Beef Lasagne": {"Menu number": "5", "Price": "£9.79"}, "Luxury Macaroni Cheese": {"Menu number": "6", "Price": "£7.49"}, "Smothered Chicken": {"Menu number": "7", "Price": "£9.79"}, "Curried Chicken Skewer": {"Menu number": "8", "Price": "£9.49"}, "Tuna Melt Sandwich": {"Menu number": "9", "Price": "£5.99"}, "Carvery": {"Menu number": "10", "Price": "£11.50"}}

# """
# Check if check_menu returns a formatted menu for browsing
# """

# def test_check_menu_returns_nicely_formatted_menu():
#     my_order = Order()
#     assert my_order.check_menu() == "Menu:\n1. Hunter's Chicken: £9.79\n2. All Day Breakfast: £9.99\n3. Farmhouse Chicken Tikka Masala: £10.79\n4. Crispy Chicken Medley: £9.79\n5. Beef Lasagne: £9.79\n6. Luxury Macaroni Cheese: £7.49\n7. Smothered Chicken: £9.79\n8. Curried Chicken Skewer: £9.49\n9. Tuna Melt Sandwich: £5.99\n10. Carvery: £11.50"

# """
# Given the menu and choosing to order item 2
# Check if add_item will update order_items
# """
# def test_adding_second_item_to_order():
#     my_order = Order()
#     my_order.add_item("2")
#     assert my_order.order == ["All Day Breakfast"]

# """
# Given the menu and choosing to order item 2 and 5
# Check if add_item will update order_items
# """

# def test_adding_second_and_fifth_item_to_order_separately():
#     my_order = Order()
#     my_order.add_item("2")
#     my_order.add_item("5")
#     assert my_order.order == ["All Day Breakfast","Beef Lasagne"]

# """
# Given the menu and choosing to order item 2 and 5
# Check if add_item will update order_items in the same add_item call
# """

# def test_adding_second_and_fifth_item_to_order_together():
#     my_order = Order()
#     my_order.add_item("2, 5")
#     assert my_order.order == ["All Day Breakfast","Beef Lasagne"]

# """
# Given the menu and choosing to order item 2 and 5 together and adding item 1 after
# Check if add_item will update order_items appropriatelly
# """

# def test_adding_second_and_fifth_item_at_once_and_first_item_after():
#     my_order = Order()
#     my_order.add_item("2, 5")
#     my_order.add_item("1")
#     assert my_order.order == ["All Day Breakfast","Beef Lasagne","Hunter's Chicken"]

# """
# Given the menu and choosing to order item 10 
# Check if add_item will update order_items with item 10 and not item 1
# """
# def test_add_item_ten_check():
#     my_order = Order()
#     my_order.add_item("10")
#     assert my_order.order == ["Carvery"]

# """
# Check if add_item raises error exception if not listed item is chosen
# """

# def test_adding_but_item_is_not_listed_so_error_message_outputs():
#     my_order = Order()
#     my_order.add_item("6")
#     with pytest.raises(Exception) as err:
#         my_order.add_item("2, 5, 17")
#     error_message = str(err.value)
#     assert error_message == "That is not a valid option."
#     assert my_order.order == ["Luxury Macaroni Cheese"]

# """
# Check if after adding items three and six to order 
# check_receipt returns a list of items as well as the total price
# """

# def test_check_receipt_after_adding_items_three_and_six():
#     my_order = Order()
#     my_order.add_item("3,   6")
#     assert my_order.check_receipt() == "Your order:\nFarmhouse Chicken Tikka Masala: £10.79\nLuxury Macaroni Cheese: £7.49\nGrand Total: £18.28"

# """
# Check if after adding item 10 to order twice
# check_receipt returns a list of items as well as the total price
# """

# def test_check_receipt_after_adding_item_ten_twice():
#     my_order = Order()
#     my_order.add_item("10, 10")
#     assert my_order.check_receipt() == "Your order:\nCarvery: £11.50\nCarvery: £11.50\nGrand Total: £23.00"

# """
# Check if check_receipt raises error exception if not items have been added to order
# """

# def test_check_receipt_error_with_no_added_items_to_order():
#     my_order = Order()
#     with pytest.raises(Exception) as err:
#         my_order.check_receipt()
#     error_message = str(err.value)
#     assert error_message == "This bitch is empty. Yeet!"

"""
Check if confirmed_text sends text message
"""