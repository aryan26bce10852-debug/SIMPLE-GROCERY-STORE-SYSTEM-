def add_item(cart):
    name = input("ENTER ITEM NAME: ")
    try:
        price = float(input("ENTER ITEM PRICE: "))
        quantity = int(input("ENTER QUANTITY: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS FOR PRICE AND QUANTITY!")
        return

    cart.append({"name": name, "price": price, "quantity": quantity})
    print(f"{quantity} x {name} added to cart.")


def remove_item(cart):
    if len(cart) == 0:
        print("Cart is empty. Nothing to remove.")
        return

    name = input("Enter the name of the item to remove: ")
    found = False

    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            found = True
            print(f"{name} removed from cart.")
            break

    if not found:
        print("Item not found in cart.")
