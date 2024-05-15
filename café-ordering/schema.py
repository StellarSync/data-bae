# Define data structures for menu items (drinks and pastries)
drink = {
  "name": str,  # Name of the drink
  "size": str,  # Size (e.g., Small, Medium, Large)
  "price": float,  # Price of the drink
}

pastry = {
  "name": str,  # Name of the pastry
  "price": float,  # Price of the pastry
}

# Define data structure for an order item (combines drink or pastry with its quantity and customizations)
order_item = {
  "name": str,  # Name of the drink or pastry
  "size": str,  # Size (applicable to drinks only)
  "price": float,  # Price of the item
  "quantity": int,  # Quantity of the item (default 1)
  "customizations": str | None,  # Optional customizations (applicable to drinks)
}

