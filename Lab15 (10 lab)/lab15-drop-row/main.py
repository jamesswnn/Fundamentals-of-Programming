#lab15-drop-row
import numpy as np

row, col = map(int, input().split())
rows = []

for i in range(row):
    values = list(map(int, input().split()))
    rows.append(np.array(values))
    
matrix = np.array(rows).reshape(row, col)

min_row_index = np.argmin(np.sum(matrix, axis=1))

output_mat = np.zeros((row - 1, col))

new_index = 0

for i in range(row):
    if i != min_row_index:
        output_mat[new_index] = matrix[i]
        new_index += 1

print(output_mat)
