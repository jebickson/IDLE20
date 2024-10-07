def intersection_of_arrays(arr_a, arr_b):
    # Convert both lists to sets to remove duplicates and allow for set operations
    set_a = set(arr_a)
    set_b = set(arr_b)
    
    # Find the intersection of both sets
    intersection = set_a.intersection(set_b)
    
    # Convert the set back to a list and return it
    return list(intersection)

# Input format
input_data = input("Enter the elements of the arrays A and B separated by a# and its elements by comma: ")
# Split the input into two parts
array_a_str, array_b_str = input_data.split('#')

# Convert the string representations of arrays into lists of integers
array_a = list(map(int, array_a_str.split(',')))
array_b = list(map(int, array_b_str.split(',')))

# Compute the intersection
result = intersection_of_arrays(array_a, array_b)

# Print the result
print("Intersection:", result)