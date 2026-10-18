'''
lab07-matrix-multiplication
'''
# YOUR CODE HERE
n = int(input())

matrix_A = []
for i in range(n):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)

    matrix_A.append(row)

martix_B = []
for i in range(n):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)

    martix_B.append(row)

martix_C = []  # สร้าง matrix เปล่าๆก่อน
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    martix_C.append(row)

for i in range(n):  # แถวmatrix A
    for j in range(n):  # คอลัมmatrix B
        for k in range(n):
            martix_C[i][j] += matrix_A[i][k] * martix_B[k][j]

print(matrix_A)
print(martix_B)
print(martix_C)
