"""receipt.py - Receipt class"""

import datetime

WIDTH = 40


class Receipt:
    def __init__(self, order, discount, discount_amount,
                 store_name="QUICK BITE FAST FOOD",
                 address="Main Street Road 143, Cebu City"):
        self.order = order
        self.discount = discount
        self.discount_amount = discount_amount
        self.store_name = store_name
        self.address = address
        self.timestamp = datetime.datetime.now().strftime("%B %d, %Y  %I:%M %p")

    @property
    def total(self):
        return self.order.subtotal - self.discount_amount

    def print(self):
        print("\n" + "=" * WIDTH)
        print(f"{self.store_name:^{WIDTH}}")
        print(f"{self.address:^{WIDTH}}")
        print(f"{self.timestamp:^{WIDTH}}")
        print("=" * WIDTH)
        print(f"{'Item':<16}{'Qty':>4}{'Price':>9}{'Total':>11}")
        print("-" * WIDTH)

        for line in self.order.lines:
            print(f"{line.item.name:<16}{line.quantity:>4}"
                  f"{line.item.price:>9.2f}{line.line_total:>11.2f}")

        print("-" * WIDTH)
        print(f"{'Subtotal:':<29}{self.order.subtotal:>11.2f}")

        if self.discount and self.discount_amount > 0:
            print(f"{self.discount.label:<29}"
                  f"{'-' + format(self.discount_amount, '.2f'):>11}")

        print(f"{'TOTAL:':<29}{self.total:>11.2f}")
        print("=" * WIDTH)
        print(f"{'Thank you for your order!':^{WIDTH}}")
        print(f"{'Please come again!':^{WIDTH}}")
        print("=" * WIDTH + "\n")