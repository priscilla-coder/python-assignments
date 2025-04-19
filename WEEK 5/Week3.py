
def calculate_discount(discount_percent):
    """
    Calculate the final price after applying a discount.
    The original price is fixed at 200.

    Parameters:
    discount_percent (float): Discount percentage to apply.

    Returns:
    float: Final price after discount if applicable, otherwise original price.
    """
    price = 200  # Fixed original price
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Fixed original price
price = 200

# Get discount percentage from user
try:
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied on original price of ${price:.2f}. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price remains: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter a number for the discount percentage.")

