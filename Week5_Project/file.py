class MMS:
    def __init__(self):
        self.order_stack = ['apple', 'mango', 'orange']
        self.inventory = {'Shan Masala': 10}

    def place_order(self, order):
        # Order processing using stack (Last-In-First-Out)
        self.order_stack.append(order)
        print(f"Order placed: {order}")

    def remove_order(self):
        x = self.order_stack.pop()
        print(f"Order removed: {x}")

    def process_order(self):
        # Pop the last order from the stack and process it
        if self.order_stack:
            order = self.order_stack.pop()
            print(f"Processing order: {order}")
            # Additional processing steps can be added

    def check_inventory(self, ingredient):
        # Check inventory levels using arrays
        if ingredient in self.inventory:
            quantity = self.inventory[ingredient]
            print(f"{ingredient} quantity: {quantity}")
        else:
            print(f"{ingredient} not found in inventory.")



current_order = 'banana'
order_system = MMS()
order_system.place_order(current_order)
order_system.remove_order()
order_system.process_order()
order_system.check_inventory('Shan Masala')