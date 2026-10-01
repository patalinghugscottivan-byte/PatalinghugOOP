"""order.py - OrderLine and Order classes"""


class OrderLine:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    @property
    def line_total(self):
        return self.item.price * self.quantity


class Order:
    def __init__(self):
        self.lines = []

    def add(self, item, quantity):
        line = OrderLine(item, quantity)
        self.lines.append(line)
        return line

    @property
    def subtotal(self):
        return sum(line.line_total for line in self.lines)