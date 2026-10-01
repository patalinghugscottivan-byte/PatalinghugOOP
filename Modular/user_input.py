"""user_input.py - validated console input"""

from menu import MENU


def ask_yes_no(prompt_message):
    while True:
        answer = input(prompt_message).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Invalid input. Please answer 'Y' for Yes or 'N' for No.")


def get_valid_menu_item():
    number_lookup = {str(i): name for i, name in enumerate(MENU, start=1)}
    lowercase_lookup = {name.lower(): name for name in MENU}

    while True:
        typed_item = input("Enter menu item number or name: ").strip()

        if typed_item in number_lookup:
            return number_lookup[typed_item]
        elif typed_item.lower() in lowercase_lookup:
            return lowercase_lookup[typed_item.lower()]
        else:
            print(f"'{typed_item}' is not a valid menu choice. Please try again.")
            print("Tip: enter the item number (e.g., 1) or the exact item name.\n")


def get_valid_quantity():
    while True:
        typed_quantity = input("Enter quantity: ").strip()
        try:
            quantity = int(typed_quantity)
            if quantity <= 0:
                print("Quantity must be a positive whole number. Try again.")
                continue
            return quantity
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")