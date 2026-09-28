def calculate_bill(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print("\nYOUR CART")
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']} - Qty: {item['quantity']} - "
              f"Price: {item['price']} - Subtotal: {item_total}")

    print(f"\nTOTAL BILL (before discount): {total}")

    discount = 0
    if total > 1500:
        discount = total * 0.25
        print("25% DISCOUNT FOR YOU MY FRIEND!")
    elif total > 1000:
        discount = total * 0.15
        print("15% DISCOUNT FOR YOU MY FRIEND!")
    elif total > 750:
        discount = total * 0.10
        print("10% DISCOUNT FOR YOU MY FRIEND!")
    elif total > 500:
        discount = total * 0.05
        print("5% DISCOUNT FOR YOU MY FRIEND!")

    final_amount = total - discount
    print(f"DISCOUNT: {discount}")
    print(f"FINAL AMOUNT TO PAY: {final_amount}")