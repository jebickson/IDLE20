def set_zeroes(matrix):
    if not matrix:
        return
    
    m, n = len(matrix), len(matrix[0])
    rows_to_zero = set()
    cols_to_zero = set()
    
    # First pass: Identify rows and columns that need to be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)

    # Second pass: Set the identified rows to zero
    for row in rows_to_zero:
        for j in range(n):
            matrix[row][j] = 0
            
    # Third pass: Set the identified columns to zero
    for col in cols_to_zero:
        for i in range(m):
            matrix[i][col] = 0

def print_matrix(matrix):
    output = []
    for row in matrix:
        output.append(row)
    print(output)

# Input format
input_data = input("Enter the matrix (columns separated by commas and rows by #): ")

# Parse input into a matrix
rows = input_data.split('#')
matrix = [list(map(int, row.split(','))) for row in rows]

# Set zeroes
set_zeroes(matrix)

# Print the modified matrix in the specified output format
print_matrix(matrix)