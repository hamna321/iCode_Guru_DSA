class McDonaldsManager:
    def __init__(self):
        # Inventory array with initial quantities
        self.inventory = {
            'burger_patties': 100,
            'buns': 150,
            'lettuce': 75,
            'tomatoes': 50,
            'staff_availability': [9, 10, 11, 12, 13, 14, 15],  # Sorted array for binary search
            'menu_items': [
                {'name': 'Cheeseburger', 'popularity': 5},
                {'name': 'Chicken McNuggets', 'popularity': 3},
                {'name': 'Big Mac', 'popularity': 7},
            ],
        }

        # Order stack
        self.order_stack = []

    def place_order(self, order):
        # Order processing using stack (Last-In-First-Out)
        self.order_stack.append(order)
        print(f"Order placed: {order}")

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

    def schedule_staff(self, shift_time):
        # Staff scheduling using binary search
        staff_availability = self.inventory['staff_availability']
        # Binary search to find available staff during the given shift time
        left, right = 0, len(staff_availability) - 1
        while left <= right:
            mid = (left + right) // 2
            if staff_availability[mid] == shift_time:
                return f"Staff available for shift at {shift_time} hours."
            elif staff_availability[mid] < shift_time:
                left = mid + 1
            else:
                right = mid - 1
        return f"No available staff for shift at {shift_time} hours."

    def sort_menu_items(self):
        # Promotions and discounts using arrays (Bubble Sort)
        menu_items = self.inventory['menu_items']
        n = len(menu_items)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if menu_items[j]['popularity'] < menu_items[j + 1]['popularity']:
                    menu_items[j], menu_items[j + 1] = menu_items[j + 1], menu_items[j]

    def display_menu(self):
        # Display menu items after sorting
        self.sort_menu_items()
        print("Menu Items:")
        for item in self.inventory['menu_items']:
            print(f"{item['name']} - Popularity: {item['popularity']}")

# Example usage
manager = McDonaldsManager()
manager.place_order('Cheeseburger')
manager.place_order('Big Mac')
manager.process_order()
manager.check_inventory('buns')
manager.schedule_staff(12)
manager.display_menu()
