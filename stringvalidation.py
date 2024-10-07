def check_character(word):
    if len(word) < 3:
        return "invalid"
    
    second_char = word[1]  # Get the second character

    if second_char.isalpha():  # Check if it's an alphabet
        if second_char.lower() in 'aeiou':  # Check if it's a vowel
            return "vowel"
        else:
            return "consonant"
    elif second_char.isdigit():  # Check if it's a digit
        return "digit"
    else:
        return "other"

# Example usage
if _name_ == "_main_":
    word = input("Enter a word: ")
    result = check_character(word)
    print(result)