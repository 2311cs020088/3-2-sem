matrix = [
    [2, 2],
    [2, 2]
]
print("Initial matrix:")
print(matrix)
for i in range(2):
    for j in range(2):
        while matrix[i][j] > 0:
            matrix[i][j] -= 1
            print(matrix)
print("Final matrix:")
print(matrix)