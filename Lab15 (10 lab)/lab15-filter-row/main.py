#lab15-filter-row
import numpy as np

row, col = map(int, input().split())
rows = []

for i in range(row):
    values = list(map(int, input().split()))
    rows.append(np.array(values))
    
matrix = np.array(rows).reshape(row, col)

threshold = int(input())

max_values = np.max(matrix, axis=1)
mesk = max_values >= threshold
result = matrix[mesk]

print(result)
