def calculate_electricity_bill(units):
    """Calculate electricity bill based on metered units."""
    if 1 <= units <= 25:
        bill = units * 1.25
    elif 26 <= units <= 50:
        bill = (25 * 1.25) + ((units - 25) * 1.45)
    elif 51 <= units <= 75:
        bill = (25 * 1.25) + (25 * 1.45) + ((units - 50) * 1.65)
    elif 76 <= units <= 95:
        bill = (25 * 1.25) + (25 * 1.45) + (25 * 1.65) + ((units - 75) * 1.95)
    elif units > 95:
        bill = (25 * 1.25) + (25 * 1.45) + (25 * 1.65) + (20 * 1.95) + ((units - 95) * 2.00)
    else:
        bill = 0  # For units <= 0, not valid based on the constraint
    
    return bill

# Input reading
U = int(input().strip())

# Validate input based on the constraints
if 0 < U < 10**6:
    bill_amount = calculate_electricity_bill(U)
    print(f"The electricity bill is: ${bill_amount:.2f}")
else:
    print("Invalid number of units. Please enter a value between 0 and 1,000,000.")