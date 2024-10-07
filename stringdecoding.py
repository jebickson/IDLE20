def decode_string(encoded):
    # Initialize the original list of characters as empty
    original = []
    
    # Process the encoded string in reverse
    for char in encoded:
        # Insert the character at the calculated middle index
        middle_index = len(original) // 2
        original.insert(middle_index, char)
    
    # Join the list into a string
    return ''.join(original)

# Input format
encoded_string = input("Enter the encoded string: ")

# Decode the string
decoded_string = decode_string(encoded_string)

# Print the decoded string
print(f"Decoded string: {decoded_string}")