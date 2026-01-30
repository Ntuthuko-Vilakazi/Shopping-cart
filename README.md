# Shopping Cart (Python)

A small command-line shopping cart system written in Python.

You can enter one item at a time using these exact prompts:
- Enter item name  
- Enter item price  
- Enter item quantity

The program uses `input`, typecasting, and formatted strings. Currency is shown as `ZAR` after calculations.

## Features
- Single-item input per run (name, price, quantity)  
- Uses `input()` with typecasting (`float` for price, `int` for quantity)  
- Prints the "You bought ..." line and a formatted total.

## Requirements
- Python 3.x

## Usage
Save the script as `shopping_cart.py` and run:

```bash
python shopping_cart.py
```

Example interaction (prompts shown exactly):

```
Enter item name: apple
Enter item price: 12.5
Enter item quantity: 3
You bought 3 apple/s
Your total is: ZAR 37.50
```

## Limitations
- Currency shown as `ZAR` only  
- Single-item flow per run  
- No extra input cleaning (inputs are used exactly as entered)  
- The prints and formatting are included verbatim per your request

## Planned upgrades (roadmap)

The project will be extended to support a more functional shopping experience. Planned improvements:

1. Multiple items per session  
   - Allow users to add multiple items in a single run and proceed to checkout when ready.  
   - Represent cart contents using a list of dictionaries, e.g. `{'name': ..., 'price': ..., 'quantity': ...}`.

2. Command-line menu interface  
   - Implement a simple menu using a `while` loop with options such as: Add Item, View Cart, Remove Item, Checkout, and Quit.  
   - Use conditional statements (`if` / `elif` / `else`) to handle menu choices and `break` to exit loops.

3. Foundational data-structure use and refactoring  
   - Use lists and dictionaries to manage cart data; refactor to small classes (e.g., `Item`, `Cart`) as my familiarity with data structures grows.

4. Input validation 
   - Validate that price and quantity are numeric and within acceptable ranges, and re-prompt the user on invalid input.

5. Cart display and totals  
   - Show line items (name, quantity, line total) and a grand total formatted to two decimal places (ZAR).

6. Future enhancements (optional)  
   - Persistence (save/load cart to JSON), improved pluralization, and unit tests for core functionality.

Note: these upgrades will be implemented progressively as the underlying concepts (lists, dictionaries, loops, and basic data structures) are learned and practiced.

## License
Note: Choose a license if you wish to publish this project.
