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

# TODO#2 - รับค่า threshold
# Your Python code goes here
threshold = int(input())

# TODO#3 - ลบแถวที่มีค่ามากที่สุดของแถวนั้นน้อยกว่า threshold
# คำใบ้:
#   1. ใช้ np.max() ที่ระบุ axis=1 เพื่อหา max ของแต่ละแถว
#   2. สร้าง boolean mask โดยเปรียบเทียบกับ threshold
#   3. ใช้ boolean mask เพื่อเลือกแถวที่ต้องการเก็บไว้
# Your Python code goes here
max_values = np.max(matrix, axis=1)
mesk = max_values >= threshold
result = matrix[mesk]

# TODO#4 - แสดงผลลัพธ์
# Your Python code goes here
print(result)