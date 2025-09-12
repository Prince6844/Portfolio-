menu = {
    'pizza': 40,
    'pasta': 30,
    'coffee': 20,
    'burger': 80
}

# Greeting
print("Welcome to the cafe")
print("Pizza: Rs40\nPasta: Rs30\nCoffee: Rs20\nBurger: Rs80\n")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ").lower()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item = ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")

print(f"The total amount of your order is Rs{order_total}")