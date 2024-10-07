def min_coins(X, Y, Z):
    # Maximum number of $5 coins we can use
    max_fives = min(Z // 5, X)

    for fives in range(max_fives, -1, -1):
        remaining_amount = Z - (fives * 5)

        # Check if we can fulfill the remaining amount with $1 coins
        if remaining_amount <= Y:
            ones = remaining_amount
            return f"Coins: $5 x {fives}, $1 x {ones}"
    
    return "NP"

# Input format
input_data = input("Enter the number of $5 coins, $1 coins, and the amount: ")
X, Y, Z = map(int, input_data.split(','))

# Validate input constraints
if not (0 < X <= 100) or not (0 < Y <= 100) or not (0 < Z <= 600):
    print("Invalid input constraints.")
else:
    # Calculate and print the result
    result = min_coins(X, Y, Z)
    print(result)