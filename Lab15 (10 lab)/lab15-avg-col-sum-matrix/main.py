# Your Python code goes here

import numpy as np

row, col = map(int, input().split())

with open('matrix.txt', 'r') as f:
    lines = f.readlines()
    
data = []

for i in range(row):
    values = lines[i].split()[:col]
    data.append(values)
    
matrix = np.array(data, dtype=np.int8)

print(matrix)
print(np.mean(matrix, axis=0))
print(np.mean(matrix, axis=1))