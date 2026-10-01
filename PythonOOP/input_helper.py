"""input_helper.py - InputHelper class (validated console input)"""


class InputHelper:
    @staticmethod
    def ask_yes_no(prompt):
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("Invalid input. Please answer 'Y' for Yes or 'N' for No.")

    @staticmethod
    def ask_quantity():
        while True:
            text = input("Enter quantity: ").strip()
            try:
                value = int(text)
            except ValueError:
                print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")
                continue
            if value <= 0:
                print("Quantity must be a positive whole number. Try again.")
                continue
            return value

    @staticmethod
    def ask_menu_item(menu):
        while True:
            text = input("Enter menu item number or name: ").strip()
            item = menu.find(text)
            if item:
                return item
            print(f"'{text}' is not a valid menu choice. Please try again.")
            print("Tip: enter the item number (e.g., 1) or the exact item name.\n")