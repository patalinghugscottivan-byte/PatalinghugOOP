"""pos_system.py - POSSystem class (runs the whole program)"""

from menu import Menu
from order import Order
from discount import BulkDiscount, SeniorPWDDiscount, DiscountEngine
from input_helper import InputHelper
from receipt import Receipt


class POSSystem:
    def __init__(self, menu=None):
        self.menu = menu or Menu.default_menu()
        self.senior_pwd_discount = SeniorPWDDiscount(rate=0.20)
        self.discount_engine = DiscountEngine(
            [BulkDiscount(threshold=500.00, rate=0.10), self.senior_pwd_discount]
        )

    def collect_order(self):
        order = Order()
        while True:
            item = InputHelper.ask_menu_item(self.menu)
            quantity = InputHelper.ask_quantity()
            line = order.add(item, quantity)
            print(f"Added: {quantity} x {item.name} = P{line.line_total:.2f}\n")

            if not InputHelper.ask_yes_no("Order another item? (Y/N): "):
                break
        return order

    def run(self):
        print("Welcome to Quick Bite Fast Food Ordering System!")
        self.menu.display()

        if not InputHelper.ask_yes_no("Would you like to place an order? (Y/N): "):
            print("\nThank you for visiting Quick Bite. Goodbye!")
            return

        order = self.collect_order()
        self.senior_pwd_discount.eligible = InputHelper.ask_yes_no(
            "Senior citizen / PWD? (Y/N): "
        )

        discount, discount_amount = self.discount_engine.best_discount(order)
        Receipt(order, discount, discount_amount).print()