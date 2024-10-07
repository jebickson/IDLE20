from itertools import permutations

def generate_permutations(array):
    # Generate all permutations using itertools.permutations
    perms = permutations(array)
    # Convert each permutation from tuple to list and then to string
    return [",".join(map(str, perm)) for perm in perms]

# Input format
input_data = input("Enter the elements of the array A separated by a comma: ")

# Convert input string to a list of integers
array = list(map(int, input_data.split(',')))

# Generate permutations
result = generate_permutations(array)

# Print all permutations separated by a comma
print(",".join(result))