# Creating a 3x3 matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

element = matrix[1][2]
print("\nElement at second row, third column:", element)

print("\nIterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
