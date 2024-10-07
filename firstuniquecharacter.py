def first_unique_character(s):
    # Step 1: Count frequency of each character
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    # Step 2: Find the first unique character
    for index, char in enumerate(s):
        if frequency[char] == 1:
            return index
            
    # Step 3: Return -1 if no unique character is found
    return -1

# Input reading
s = input().strip()
result = first_unique_character(s)
print(result)