from display import show_menu
from cart_manager import add_item, remove_item
from billing import calculate_bill

cart = []

def main():
    while True:
        show_menu()
        choice = input("ENTER YOUR CHOICE (1-4): ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            calculate_bill(cart)
        elif choice == "4":
            print("THANK YOU FOR SHOPPING WITH US! PLEASE VISIT AGAIN!")
            break
        else:
            print("WRONG ATTEMPT. PLEASE TRY AGAIN.")


if __name__ == "__main__":
    main()