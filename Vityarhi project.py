
cart = []  

def DISPLAY_SCREEN():
    print("\nSIMPLE GROCERY STORE SYSTEM")
    print("1. ADD ITEMS TO CART")
    print("2. REMOVE ITEMS FROM CART")
    print("3. VIEW YOUR BILL")
    print("4. EXIT")


def add_item():
    name = input("ENTER ITEM NAME: ")
    try:
        price = float(input("ENTER ITEM PRICE: "))
        quantity = int(input("ENTER QUANTITY: "))
    except ValueError:
        print("INVALID INPUT! :( PLEASE NUMBERS FOE PRICE AND YOUR ITEMS!!! :)")
        return

    item = {"name": name, "price": price, "quantity": quantity}
    cart.append(item)
    print(f"{quantity} x {name} added to cart.")


def remove_item():
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


def calculate_bill():
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print("\nYOUR CART")
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']} - Qty: {item['quantity']} - Price: {item['price']} - Subtotal: {item_total}")

    print(f"\nTOTAL BILL(before discount): {total}")

    discount = 0
    if total > 500:
        discount = total * 0.05   
        print("5% DISOUNT FOR YOU MY FRIEND!")
    elif total > 750:
        discount = total * 0.10 
        print("10% DISOUNT FOR YOU MY FRIEND!") 
    elif total > 1000:
        discount = total * 0.15     
        print("15% DISOUNT FOR YOU MY FRIEND!")
    elif total > 1500:
        discount = total * 0.25
        print("25% DISOUNT FOR YOU MY FRIEND!")

    TOTAL_AMOUNT_TO_BE_PAID = total - discount
    print(f"DISCOUNT: {discount}")
    print(f"FINAL AMOUNT TO PAY: {TOTAL_AMOUNT_TO_BE_PAID}")


def main():
    while True:
        DISPLAY_SCREEN()
        choice = input("ENTER YOUR CHOICE (1-4):" )

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            calculate_bill()
        elif choice == "4":
            print("THANK YOU FOR SHOPPING WITH US!! PLEASE VISIT OUR SITE AGAIN !! THANK YOU VERY MUCH HAVE A NICE DAY !!! :) :) :)" )
    
            break
        else:
            print("WRONG ATTEMPT . PLEASE TRY AGAIN . :(")
                  
main()