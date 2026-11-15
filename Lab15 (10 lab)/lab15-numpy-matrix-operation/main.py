#lab15-numpy-matrix-operation
import numpy as np

file_A = input()
file_B = input()
file_C = input()

def read_matrix(file):
    with open('data/' + file, 'r') as f:
        lines = f.readlines()
    
    rows = []
    for line in lines:
        rows.append(line.split())
    return np.array(rows, dtype=int)

A = read_matrix(file_A)
B = read_matrix(file_B)
C = read_matrix(file_C)

if A.shape == B.shape and A.shape[1] == C.shape[0]:
    print((A + B) @ C)
else:
    print(f"A: {A.shape}")
    print(f"B: {B.shape}")
    print(f"C: {C.shape}")
    print("Invalid matrix dimensions")
