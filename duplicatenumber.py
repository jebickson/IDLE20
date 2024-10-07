def find_duplicate(arr):
    seen = set()  # To store numbers we've encountered

    for num in arr:
        if num in seen:
            return num  # If we see a number again, it's the duplicate
        seen.add(num)  # Add the number to the set

    return -1  # If no duplicates were found

# Input format
input_data = input("Enter the elements of the array separated by commas: ")
# Convert the input string to a list of integers
array = list(map(int, input_data.split(',')))

# Find and print the duplicate number
duplicate = find_duplicate(array)
print(duplicate)