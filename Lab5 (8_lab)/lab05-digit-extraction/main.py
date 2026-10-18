'''
lab05-digit-extraction
'''

# YOUR CODE HERE
x = int(input())
count = 0

last_digit = x % 10  # เลขที่เหลือสุดท้ายเป็นหลักสุดท้าย

while x > 0:
    first_digit = x % 10  # เลขที่เหลือสุดท้ายเป็นหลักแรก
    x = x // 10  # ลบไปทีละหลัก เพื่อหาจำนวนหลัก
    count = count + 1

print(f"{count} {first_digit} {last_digit} {first_digit + last_digit}")