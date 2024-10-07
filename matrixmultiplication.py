def matrix_multiply(M1, M2, N):
    # Initialize the result matrix with zeros
    result = [[0] * N for _ in range(N)]
    
    # Perform matrix multiplication
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += M1[i][k] * M2[k][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(",".join(map(str, row)))

# Input format
input_data = input("Enter the size of matrix N and the matrices separated by '@': ")

# Parse the input
n, matrices = input_data.split('@')
N = int(n)

# Split the matrices by '#'
matrices = matrices.strip().split('#')
M1 = []
M2 = []

# Fill the first matrix
for i in matrices[0].strip().split('#'):
    M1.append(list(map(int, i.split(','))))

# Fill the second matrix
for i in matrices[1].strip().split('#'):
    M2.append(list(map(int, i.split(','))))

# Ensure both matrices are N x N
if len(M1) != N or len(M2) != N or any(len(row) != N for row in M1) or any(len(row) != N for row in M2):
    print("Matrices are not of size N x N.")
else:
    # Calculate the product of the two matrices
    product_matrix = matrix_multiply(M1, M2, N)

    # Print the resulting product matrix
    print("Product of the matrices:")
    print_matrix(product_matrix)