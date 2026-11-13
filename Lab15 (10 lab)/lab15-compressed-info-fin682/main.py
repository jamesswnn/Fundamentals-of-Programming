### START import
# ถ้า นศ ต้องการ Import Python Library สามารถทำได้ในส่วนนี้
import numpy as np
#### END import



#### START Functions

## TODO 2: เขียนฟังก์ชัน `encode_data` เพื่อบีบอัดข้อมูล
def encode_data(arr1, arr2):
    diff = np.array(arr1) - np.array(arr2)

    encoding = []
    count = 1

    for i in range(1, len(diff)):
        if diff[i] == diff[i - 1]:
            count += 1
        else:
            encoding.append((int(diff[i - 1]), count))
            count = 1

    encoding.append((int(diff[-1]), count))

    return encoding
        
## END TODO 2

#### END Functions



#### START Main Program

## TODO 1: อ่านข้อมูล input 2 บรรทัด
#          บรรทัด1 เก็บใน arr1, บรรทัด 2 เก็บใน arr2
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

## END TODO 1

## TODO 3: เรียกใช้ฟังก์ชัน `encode_data` ที่เขียนไว้ใน TODO 2
#          เก็บผลลัพธ์ในตัวแปร `out_enc`
out_enc = encode_data(arr1, arr2)
## END TODO 3

# แสดงผลลัพธ์
print('Sender sent:')
print(' First input: ', end='')
for v in arr1: print(v, end=' ')
print()
print(f' Encode data: {out_enc}')

#### END Main Program