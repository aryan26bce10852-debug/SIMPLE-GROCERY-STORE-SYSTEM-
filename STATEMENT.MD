# Project Statement: Simple Grocery Store System

## Problem Statement

Small grocery stores often prepare customer bills by hand or with a basic calculator. This is slow and leads to calculation mistakes. Discounts are applied inconsistently, and it is difficult to correct an order once items have been written down.

This project solves the problem with a simple Python program. The user can build a cart of items, remove items that are not needed, and get an accurate, itemised bill. The correct discount is applied automatically based on the total amount.

## Scope of the Project

### In Scope
- Adding items to a cart with a name, price and quantity.
- Removing items from the cart by name (not case-sensitive).
- Calculating each item's subtotal and the total bill.
- Applying a tiered discount automatically:

  | Total Bill | Discount |
  |------------|----------|
  | Above 500  | 5%       |
  | Above 750  | 10%      |
  | Above 1000 | 15%      |
  | Above 1500 | 25%      |

- Validating inputs so that wrong entries do not crash the program.
- A menu-driven, command-line interface that runs until the user exits.

### Out of Scope
- Saving data permanently (no database or file storage).
- A graphical or web interface.
- Stock management, user login, tax (GST) calculation and online payments.

## Target Users

- **Small shop owners and cashiers** who need a quick and simple way to prepare bills.
- **Students and beginners** learning Python who want a practical example using functions, lists, dictionaries, loops and exception handling.
- **Customers**, who get a clear itemised bill with the discount shown.

## High-Level Features

- **Add items:** enter the item name, price and quantity.
- **Remove items:** delete an item from the cart by name.
- **View bill:** see each item with its quantity, price and subtotal, followed by the total.
- **Automatic discount:** the discount slab is chosen from the total and applied to the final amount.
- **Input validation:** invalid prices, quantities and menu choices show a message instead of crashing.
- **Menu-driven interface:** the program keeps running until the user chooses Exit.