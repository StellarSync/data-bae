def add_drink_to_order(order, drinks, drink_name, size, customizations=None):
  """Adds a drink to the order, considering size and customizations."""
  for drink in drinks:
    if drink["name"].lower() == drink_name.lower() and drink["size"] == size:
      drink_to_add = drink.copy() 
      if customizations:
        drink_to_add["customizations"] = customizations
      order.append(drink_to_add)
      print(f"{drink_name} ({size}) added to your order!")
      return  

  print(f"Sorry, we don't have '{drink_name}' in size '{size}'.")

def add_pastry_to_order(order, pastries, pastry_name, quantity=1):
  """Adds a pastry to the order, considering quantity."""
  for pastry in pastries:
    if pastry["name"].lower() == pastry_name.lower():
      pastry_to_add = pastry.copy()
      pastry_to_add["quantity"] = quantity
      order.append(pastry_to_add)
      print(f"{quantity} {pastry_name} added to your order!")
      return 
  print(f"Sorry, we don't have '{pastry_name}' available.")

def remove_item_from_order(order, item_name):
  """Removes an item (drink or pastry) from the order by name."""
  for i, item in enumerate(order):
    if item["name"].lower() == item_name.lower():
      removed_item = order.pop(i)
      print(f"{removed_item['name']} removed from your order.")
      return 

  print(f"{item_name} not found in your order.")

def display_order(order):
  """Displays the current order details."""
  if not order:
    print("Your order is currently empty.")
    return

  print("\nYour Order:")
  total_cost = 0
  for item in order:
    name = item["name"]
    size = item.get("size", "")  
    quantity = item.get("quantity", 1) 
    price = item["price"]
    customizations = item.get("customizations", None)

    print(f"- {quantity} {name} ({size}) {customizations if customizations else ''}: ${price:.2f}")
    total_cost += price * quantity

  print(f"\nTotal: ${total_cost:.2f}")

def calculate_total_cost(order):
  """Calculates the total cost of the order."""
  total_cost = 0
  for item in order:
    price = item["price"]
    quantity = item.get("quantity", 1)  
    total_cost += price * quantity
  return total_cost

