def minimum_swaps(arr):
    n = len(arr)
    arr_pos = [(value, index) for index, value in enumerate(arr)]
    
    # Sort the array based on the values
    arr_pos.sort(key=lambda x: x[0])
    
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # If already visited or in the correct position, skip
        if visited[i] or arr_pos[i][1] == i:
            continue
            
        cycle_size = 0
        j = i
        
        # Count the size of the cycle
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1
        
        # If there is a cycle of size 'n', we need (n-1) swaps
        if cycle_size > 0:
            swaps += (cycle_size - 1)
    
    return swaps

# Input format
input_data = input("Enter the set of integers separated by commas: ")
arr = list(map(int, input_data.split(',')))

# Calculate and print the minimum number of swaps
result = minimum_swaps(arr)
print(f"Minimum number of swaps required: {result}")