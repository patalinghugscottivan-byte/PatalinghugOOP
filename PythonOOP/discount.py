"""discount.py - Discount classes"""

from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, label, rate):
        self.label = label
        self.rate = rate

    @abstractmethod
    def is_applicable(self, order):
        """Return True if this discount can be applied to the order."""

    def amount(self, order):
        return order.subtotal * self.rate if self.is_applicable(order) else 0.00


class BulkDiscount(Discount):
    def __init__(self, threshold=500.00, rate=0.10):
        super().__init__(f"Bulk Order Discount ({int(rate * 100)}%)", rate)
        self.threshold = threshold

    def is_applicable(self, order):
        return order.subtotal >= self.threshold


class SeniorPWDDiscount(Discount):
    def __init__(self, rate=0.20):
        super().__init__(f"Senior/PWD Discount ({int(rate * 100)}%)", rate)
        self.eligible = False

    def is_applicable(self, order):
        return self.eligible


class DiscountEngine:
    """Picks the single best discount from a list of discounts."""

    def __init__(self, discounts):
        self.discounts = discounts

    def best_discount(self, order):
        best, best_amount = None, 0.00
        for discount in self.discounts:
            amount = discount.amount(order)
            if amount > best_amount:
                best, best_amount = discount, amount
        return best, best_amount