# Simple program to calculate discount

def calculate_discount(price, discount_percent):
    # if discount is 20% or more, apply it
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # no discount if less than 20%
        return price


# Ask user for inputs
price_input = float(input("Enter the original price of the item: "))
discount_input = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price_input, discount_input)

# Print result
if discount_input >= 20:
    print("Final price after discount is:", final_price)
else:
    print("No discount applied. The price is:", final_price)
