# SIMPLE-GROCERY-STORE-SYSTEM-
A beginner friendly Python Project for managing Grocery items and calculating bills. It allow users to view available grocery items and their prices. The system calculates the total cost of the selected items. This project helps demonstrate basic Python concepts such as loops, lists, dictionaries and conditional statements. 


# Simple Grocery Store System

## Overview

The Simple Grocery Store System is a command-line application written in Python. It lets a customer build a shopping cart by adding and removing grocery items, then generates a bill that automatically applies a discount based on the total amount. The project demonstrates core Python concepts: functions, lists, dictionaries, loops, conditionals, input validation and exception handling.

## Features

- **Add items to cart:** enter an item name, price and quantity.
- **Remove items from cart:** remove an item by name (case-insensitive).
- **View bill:** shows each item with its quantity, price and subtotal, followed by the total.
- **Tiered discounts:** applied automatically on the total bill.
  | Total Bill | Discount |
  |------------|----------|
  | Above 500  | 5%       |
  | Above 750  | 10%      |
  | Above 1000 | 15%      |
  | Above 1500 | 25%      |
- **Input validation:** invalid price or quantity is caught with `try/except` and the program continues without crashing.
- **Menu-driven interface:** runs in a loop until the user chooses to exit.

## Technologies / Tools Used

- **Language:** Python 3.x
- **Data structures:** list (cart) and dictionaries (items)
- **Editor/IDE:** any (VS Code, PyCharm, IDLE, etc.)
- **Version control:** Git & GitHub

No external libraries are required.


## Instructions for Testing

Run the program and try these test cases:

| # | Action | Input | Expected Result |
|---|--------|-------|-----------------|
| 1 | Add item | Rice, 60, 2 | "2 x Rice added to cart." |
| 2 | Invalid price | Milk, abc | "INVALID INPUT!" message, cart unchanged |
| 3 | Invalid quantity | Milk, 50, two | "INVALID INPUT!" message, cart unchanged |
| 4 | View empty cart | Option 3 with empty cart | "Your cart is empty." |
| 5 | Remove item | Option 2, Rice | "Rice removed from cart." |
| 6 | Remove missing item | Option 2, Sugar | "Item not found in cart." |
| 7 | Remove from empty cart | Option 2 with empty cart | "Cart is empty. Nothing to remove." |
| 8 | No discount | Total of 400 | Discount 0, final = 400 |
| 9 | 5% discount | Total of 600 | Discount 30, final = 570 |
| 10 | 10% discount | Total of 800 | Discount 80, final = 720 |
| 11 | 15% discount | Total of 1200 | Discount 180, final = 1020 |
| 12 | 25% discount | Total of 2000 | Discount 500, final = 1500 |
| 13 | Invalid menu choice | Enter 9 | "WRONG ATTEMPT. PLEASE TRY AGAIN." |
| 14 | Exit | Option 4 | Thank-you message, program ends |

## Sample Output

```
SIMPLE GROCERY STORE SYSTEM
1. ADD ITEMS TO CART
2. REMOVE ITEMS FROM CART
3. VIEW YOUR BILL
4. EXIT
ENTER YOUR CHOICE (1-4): 3

YOUR CART
Rice - Qty: 2 - Price: 60.0 - Subtotal: 120.0

TOTAL BILL(before discount): 120.0
DISCOUNT: 0
FINAL AMOUNT TO PAY: 120.0
```



## Author

Your Name : ARYAN SINGH 
Register Number: 26BCE10852
