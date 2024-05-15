from database import (
    add_drink_to_order, add_pastry_to_order, remove_item_from_order,
    display_order, calculate_total_cost
)

def display_menu(drinks, pastries):
    """Displays the café menu with drinks and pastries."""
    print("Coffee Drinks:")
    for drink in drinks:
        print(f"- {drink['name']} ({drink['size']}): ${drink['price']}")

    print("\nPastries:")
    for pastry in pastries:
        print(f"- {pastry['name']}: ${pastry['price']}")

def take_order(drinks, pastries):
    """Prompts the user to create and manage their order."""
    order = []
    while True:
        display_menu(drinks, pastries)
        choice = input("Enter 'd' to order drinks, 'p' for pastries, 'v' to view order, 'r' to remove items, 'q' to quit: ").lower()

        if choice == 'd':
            # Implement logic to add drinks to the order (consider size, customizations)
            pass
        elif choice == 'p':
            # Implement logic to add pastries to the order (consider quantity)
            pass
        elif choice == 'v':
            # Display the current order details (name, size, price, quantity, customizations)
            pass
        elif choice == 'r':
            # Implement logic to remove items from the order
            pass
        elif choice == 'q':
            break
        else:
            print("Invalid input. Please enter a valid option.")

    # Calculate the total order cost
    total_cost = 0
    # Implement logic to iterate through the order and calculate total cost

    print(f"\nYour order total is: ${total_cost:.2f}")

def main():
    """The main entry point of the program."""
       drinks = [
        {"name": "Coffee", "size": "Small", "price": 1.50},
        {"name": "Coffee", "size": "Medium", "price": 2.00},
        {"name": "Coffee", "size": "Large", "price": 2.50},
        {"name": "Latte", "size": "Small", "price": 2.25},
        {"name": "Latte", "size": "Medium", "price": 3.00},
        {"name": "Latte", "size": "Large", "price": 3.50},
        {"name": "Cappuccino", "size": "Small", "price": 2.50},
        {"name": "Cappuccino", "size": "Medium", "price": 3.25},
        {"name": "Cappuccino", "size": "Large", "price": 3.75},
    ]
    pastries = [
        {"name": "Croissant", "price": 1.00},
        {"name": "Muffin", "price": 1.25},
        {"name": "Pancake", "price": 3.25},
        {"name": "Cookie", "price": 0.75},
    ]

    take_order(drinks, pastries)

if __name__ == "__main__":
    main()

