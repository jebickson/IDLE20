def remove_characters(s):
    # Generate the sequence of indices (2^n) that are within the length of the string
    indices_to_remove = []
    n = 0
    while True:
        index = 2 ** n
        if index < len(s):
            indices_to_remove.append(index)
            n += 1
        else:
            break
    
    # Remove the characters at the specified indices
    result = ''.join(s[i] for i in range(len(s)) if i not in indices_to_remove)
    
    return result

# Example usage
input_string = "Infosys global"
output_string = remove_characters(input_string)
print(output_string)