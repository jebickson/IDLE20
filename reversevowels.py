def reverse_vowels(s):
    # Step 1: Define the set of vowels
    vowels = set("aeiouAEIOU")
    
    # Step 2: Extract vowels from the string
    vowel_list = [char for char in s if char in vowels]
    
    # Step 3: Reverse the list of vowels
    vowel_list.reverse()
    
    # Step 4: Reconstruct the string with reversed vowels
    result = []
    vowel_index = 0
    
    for char in s:
        if char in vowels:
            result.append(vowel_list[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

# Input reading
s = input().strip()
result = reverse_vowels(s)
print(result)