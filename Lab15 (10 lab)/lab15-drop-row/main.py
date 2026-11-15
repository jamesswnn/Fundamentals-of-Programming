#lab15-drop-row

import numpy as np

# TODO#1 - รับข้อมูล 2D Array
# คำใบ้:
#   1. อ่านค่าจาก input() แถวแรกเพื่อรับขนาดของ array (row, col)
#   2. ใช้ลูป for เพื่ออ่านข้อมูลแต่ละแถว
#   3. แปลงข้อมูลเป็น int และเก็บใน list
#   4. สร้าง numpy array จาก list ที่ได้
# Your Python code goes here
row, col = map(int, input().split())
rows = []

for i in range(row):
    values = list(map(int, input().split()))
    rows.append(np.array(values))
    
matrix = np.array(rows).reshape(row, col)

# TODO#2 - หาตำแหน่งแถวที่ผลรวมต่ำสุด
# คำใบ้:
#   1. ใช้ np.sum() ที่ระบุ axis เพื่อหาผลรวมของแต่ละแถว
#   2. ใช้ np.argmin() เพื่อหาตำแหน่งของแถวที่มีผลรวมต่ำสุด
# Your Python code goes here
min_row_index = np.argmin(np.sum(matrix, axis=1))

# TODO#3 - ทำการสร้าง 2D array ใหม่ ที่ไม่มีแถวที่ผลรวมต่ำสุด
# คำใบ้:
#   1. สร้าง array เปล่าขนาด (row-1, col) ด้วย np.zeros()
#   2. คัดลอกข้อมูลจาก input_mat ไปยัง output_mat โดยข้ามแถวที่มีผลรวมต่ำสุด
# Your Python code goes here
output_mat = np.zeros((row - 1, col))

new_index = 0

for i in range(row):
    if i != min_row_index:
        output_mat[new_index] = matrix[i]
        new_index += 1


# TODO#4 - แสดงผลลัพธ์ด้วย output_mat
# Your Python code goes here
print(output_mat)