# 06_store_simulation.py
"""
Simple Store Simulation: Buy Computer Parts
---------------------------------------------

This script simulates a user selecting computer parts from a store.
It shows available items, lets the user add items to their cart,
and calculates the total cost.
"""

print("Welcome to the store!")
computer_parts = []
total_cost = 0

# Dictionary of available items with their costs
items_available = {
    "1": ("Laptop", 29250),
    "2": ("Monitor", 12500),
    "3": ("CPU", 15000),
    "4": ("Keyboard", 1000),
    "5": ("Mouse", 500),
    "6": ("Mouse Pad", 250)
}

def show_menu():
    print("\nAvailable items to add:")
    for key, (item, cost) in items_available.items():
        print(f"Press {key} to add {item} (Cost: {cost})")
    print("Press 0 to checkout and exit")

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "0":
        break

    if choice in items_available:
        item, cost = items_available[choice]
        computer_parts.append(item)
        total_cost += cost
        print(f"Added {item} to your cart. Current total: {total_cost}")
    else:
        print("Invalid choice, please try again.")

print("\nYour final cart:")
for item in computer_parts:
    print(f"- {item}")

print(f"Total cost: {total_cost}")
print("Thank you for shopping with us!")
