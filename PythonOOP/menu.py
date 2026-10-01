"""menu.py - MenuItem and Menu classes"""

WIDTH = 40


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_by_number(self, number):
        if 1 <= number <= len(self._items):
            return self._items[number - 1]
        return None

    def get_by_name(self, name):
        for item in self._items:
            if item.name.lower() == name.lower():
                return item
        return None

    def find(self, text):
        """Find an item by number or by name."""
        text = text.strip()
        if text.isdigit():
            return self.get_by_number(int(text))
        return self.get_by_name(text)

    def display(self):
        print("\n" + "=" * WIDTH)
        print(f"{'FAST FOOD MENU':^{WIDTH}}")
        print("=" * WIDTH)
        print(f"{'#':<4}{'Item':<21}{'Price':>15}")
        print("-" * WIDTH)
        for number, item in enumerate(self._items, start=1):
            print(f"{number:<4}{item.name:<21}{'P' + format(item.price, '.2f'):>15}")
        print("=" * WIDTH + "\n")

    @classmethod
    def default_menu(cls):
        menu = cls()
        for name, price in [
            ("Cheeseburger", 89.00),
            ("Chicken Sandwich", 99.00),
            ("French Fries", 55.00),
            ("Onion Rings", 60.00),
            ("Nuggets (6pc)", 95.00),
            ("Cola (Regular)", 35.00),
            ("Iced Tea (Regular)", 35.00),
            ("Sundae", 40.00),
            ("Apple Pie", 45.00),
        ]:
            menu.add_item(MenuItem(name, price))
        return menu