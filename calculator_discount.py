def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount percentage is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(original_price, discount)

    # Display result
    if final_price == original_price:
        print(f"No discount applied. Final price: {final_price:.2f}")
    else:
        print(f"Discount applied! Final price after {discount}% discount is: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
