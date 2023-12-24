print('''
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──██████─██████████████─██████──────────██████─████████████───██████████─██████──────────██████─██████████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░████─██░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████████─██░░░░░░░░░░██──██░░██─██░░████░░░░██─████░░████─██░░░░░░░░░░██──██░░██─██░░██████████─
─██░░██──██░░██─██░░██─────────██░░██████░░██──██░░██─██░░██──██░░██───██░░██───██░░██████░░██──██░░██─██░░██─────────
─██░░██──██░░██─██░░██████████─██░░██──██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██─────────
─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██████─
─██░░██──██░░██─██░░██████████─██░░██──██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██░░██─
─██░░░░██░░░░██─██░░██─────────██░░██──██░░██████░░██─██░░██──██░░██───██░░██───██░░██──██░░██████░░██─██░░██──██░░██─
─████░░░░░░████─██░░██████████─██░░██──██░░░░░░░░░░██─██░░████░░░░██─████░░████─██░░██──██░░░░░░░░░░██─██░░██████░░██─
───████░░████───██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░████─██░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─
─────██████─────██████████████─██████──────────██████─████████████───██████████─██████──────────██████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─██████████████─██████──██████─██████████─██████──────────██████─██████████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░██████████─██░░██──██░░██─████░░████─██░░░░░░░░░░██──██░░██─██░░██████████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██───██░░██───██░░██████░░██──██░░██─██░░██─────────
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██─────────██░░██████░░██───██░░██───██░░██──██░░██──██░░██─██░░██████████─
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─██░░░░░░░░░░██─
─██░░██──██████──██░░██─██░░██████░░██─██░░██─────────██░░██████░░██───██░░██───██░░██──██░░██──██░░██─██░░██████████─
─██░░██──────────██░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██───██░░██───██░░██──██░░██████░░██─██░░██─────────
─██░░██──────────██░░██─██░░██──██░░██─██░░██████████─██░░██──██░░██─████░░████─██░░██──██░░░░░░░░░░██─██░░██████████─
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─
─██████──────────██████─██████──██████─██████████████─██████──██████─██████████─██████──────────██████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')
class VendingMachine:
    def __init__(self):
        self.menu = {
            'M1': {'item': 'Cola', 'price': 1.50, 'quantity': 10},
            'P2': {'item': 'Chips', 'price': 1.00, 'quantity': 8},
            'Q1': {'item': 'Cold coffee', 'price': 1.20, 'quantity': 12},
            'D2': {'item': 'protein bar', 'price': 3.30, 'quantity': 15},
        }
        self.money_in_machine = 50.0  # Initial amount in the machine
        self.transaction_history = []

    def display_menu(self):
        print("==== Vending Machine Menu ====")
        for code, details in self.menu.items():
            print(f"{code}: {details['item']} - ${details['price']:.2f} ({details['quantity']} left)")

    def process_selection(self):
        selection = input("Enter the code of the item you want to purchase: ")
        if selection in self.menu and self.menu[selection]['quantity'] > 0:
            item_details = self.menu[selection]
            return item_details
        elif selection in self.menu and self.menu[selection]['quantity'] == 0:
            print("Sorry, this item is out of stock.")
            return None
        else:
            print("Invalid selection. Please try again.")
            return None

    def accept_money(self):
        money_inserted = float(input("Insert money (in dollars): "))
        return money_inserted

    def dispense_item(self, item):
        print(f"\nDispensing {item['item']}. Enjoy!")
        item['quantity'] -= 1

    def give_change(self, money_inserted, item_price):
        change = money_inserted - item_price
        print(f"Change: ${change:.2f}")
        return change

    def update_transaction_history(self, item, money_inserted, change):
        transaction = {
            'item': item['item'],
            'price': item['price'],
            'money_inserted': money_inserted,
            'change': change,
        }
        self.transaction_history.append(transaction)

    def display_transaction_history(self):
        print("\n==== Transaction History ====")
        for transaction in self.transaction_history:
            print(f"Item: {transaction['item']}, Price: ${transaction['price']:.2f}, "
                  f"Money Inserted: ${transaction['money_inserted']:.2f}, Change: ${transaction['change']:.2f}")

    def run_vending_machine(self):
        while True:
            self.display_menu()
            selected_item = self.process_selection()

            if selected_item:
                item_price = selected_item['price']
                money_inserted = self.accept_money()

                if money_inserted >= item_price:
                    self.dispense_item(selected_item)
                    change = self.give_change(money_inserted, item_price)
                    self.money_in_machine += item_price
                    self.money_in_machine -= change
                    self.update_transaction_history(selected_item, money_inserted, change)

                else:
                    print("Insufficient funds. Transaction canceled.")

            another_transaction = input("Do you want to make another transaction? (yes/no): ").lower()
            if another_transaction != 'yes':
                print("Thank you for using the Vending Machine!")
                self.display_transaction_history()
                break


# Instantiate the VendingMachine class
vending_machine = VendingMachine()

# Run the vending machine
vending_machine.run_vending_machine()