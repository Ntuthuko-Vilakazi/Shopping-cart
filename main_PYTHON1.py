#Ask user for item details
item= input('Enter item name:')
price= float(input('Enter item price:'))
quantity= int(input('Enter item quantity:'))

# Calculate the total
total= price * quantity

# Show results with currency formatting
print(f'You bought {quantity}{item}/s')
print(f'Your total is: ZAR {round (total,2)}')