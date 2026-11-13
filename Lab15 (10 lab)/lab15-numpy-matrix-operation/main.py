import numpy as np

# 1. รับชื่อไฟล์ของ A, B และ C
# 2. อ่านข้อมูลจากไฟล์
# 3. ตรวจสอบ dimension
# 4. หาก dimension ไม่ถูกต้อง ให้พิมพ์ shape ของ A, B และ C และข้อความ ข้อความ Invalid matrix dimensions
# 5. หาก dimension ถูกต้อง แสดงผล (A + B) @ C 

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
