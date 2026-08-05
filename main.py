import json
from pathlib import Path

DATA_FILE = Path("inventory.json")


def load_inventory():
    """Load saved inventory from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Inventory data could not be loaded. Starting with an empty list.")
        return []


def save_inventory(inventory):
    """Save inventory to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)


def get_next_id(inventory):
    """Create the next available inventory ID."""
    if not inventory:
        return 1

    return max(item["id"] for item in inventory) + 1


def add_item(inventory):
    """Add a new item to the inventory."""
    print("\n--- Add Item ---")

    name = input("Item name: ").strip()

    if not name:
        print("The item name cannot be empty.")
        return

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price: $"))

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    item = {
        "id": get_next_id(inventory),
        "name": name,
        "quantity": quantity,
        "price": price,
    }

    inventory.append(item)
    save_inventory(inventory)

    print(f"{name} was added successfully.")


def view_inventory(inventory):
    """Display every item in the inventory."""
    print("\n--- Current Inventory ---")

    if not inventory:
        print("No inventory items have been added.")
        return

    print(f"{'ID':<5}{'Name':<25}{'Quantity':<12}{'Price':<12}{'Total Value'}")
    print("-" * 68)

    for item in inventory:
        total_value = item["quantity"] * item["price"]

        print(
            f"{item['id']:<5}"
            f"{item['name']:<25}"
            f"{item['quantity']:<12}"
            f"${item['price']:<11.2f}"
            f"${total_value:.2f}"
        )


def search_inventory(inventory):
    """Search for inventory items by name."""
    print("\n--- Search Inventory ---")

    search_term = input("Enter an item name: ").strip().lower()

    matches = [
        item
        for item in inventory
        if search_term in item["name"].lower()
    ]

    if not matches:
        print("No matching items were found.")
        return

    view_inventory(matches)


def update_item(inventory):
    """Update an existing inventory item."""
    print("\n--- Update Item ---")

    try:
        item_id = int(input("Enter the item ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    item = next(
        (current_item for current_item in inventory if current_item["id"] == item_id),
        None,
    )

    if item is None:
        print("Item not found.")
        return

    print("Leave a field blank to keep the current value.")

    new_name = input(f"Name [{item['name']}]: ").strip()
    new_quantity = input(f"Quantity [{item['quantity']}]: ").strip()
    new_price = input(f"Price [{item['price']:.2f}]: $").strip()

    if new_name:
        item["name"] = new_name

    try:
        if new_quantity:
            quantity = int(new_quantity)

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            item["quantity"] = quantity

        if new_price:
            price = float(new_price)

            if price < 0:
                print("Price cannot be negative.")
                return

            item["price"] = price

    except ValueError:
        print("Quantity and price must be valid numbers.")
        return

    save_inventory(inventory)
    print("Item updated successfully.")


def delete_item(inventory):
    """Delete an item from the inventory."""
    print("\n--- Delete Item ---")

    try:
        item_id = int(input("Enter the item ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    item = next(
        (current_item for current_item in inventory if current_item["id"] == item_id),
        None,
    )

    if item is None:
        print("Item not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete {item['name']}? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        inventory.remove(item)
        save_inventory(inventory)
        print("Item deleted successfully.")
    else:
        print("Delete canceled.")


def show_low_stock(inventory):
    """Display items with a quantity of five or less."""
    print("\n--- Low-Stock Items ---")

    low_stock_items = [
        item for item in inventory if item["quantity"] <= 5
    ]

    if not low_stock_items:
        print("There are no low-stock items.")
        return

    view_inventory(low_stock_items)


def show_menu():
    print(
        "\n===== InventoryPro =====\n"
        "1. Add an item\n"
        "2. View inventory\n"
        "3. Search inventory\n"
        "4. Update an item\n"
        "5. Delete an item\n"
        "6. View low-stock items\n"
        "7. Exit"
    )


def main():
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            search_inventory(inventory)
        elif choice == "4":
            update_item(inventory)
        elif choice == "5":
            delete_item(inventory)
        elif choice == "6":
            show_low_stock(inventory)
        elif choice == "7":
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Please choose a number from 1 through 7.")


if __name__ == "__main__":
    main()
