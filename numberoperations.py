def process_number(X):
    # Check if the number is a single digit
    if 0 <= X < 10:
        return X ** 2  # Return the square of the number
    else:
        # Convert the number to string to access digits
        str_X = str(X)
        
        # Get the second digit if it exists
        if len(str_X) > 1:
            second_digit = int(str_X[1])  # Get the second digit
            
            # Check divisibility
            if second_digit % 2 == 0 and second_digit % 4 == 0:
                return "24"
            elif X % 2 == 0:
                return "2"
            else:
                return "1"

# Example usage
if _name_ == "_main_":
    X = int(input("Enter a number (1 <= X <= 9999): "))
    
    if 1 <= X <= 9999:
        result = process_number(X)
        print(result)
    else:
        print("Number out of bounds.")