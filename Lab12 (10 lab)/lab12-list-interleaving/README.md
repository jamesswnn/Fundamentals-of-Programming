## List Interleaving
จงเขียนโปรแกรมที่รับตัวเลขจำนวน `n1` และ `n2` ตัว โดยใช้ **loop** เพื่อเก็บข้อมูลตัวเลขใน list `list1` และ `list2`  

จากนั้นโปรแกรมจะเรียกใช้ function `list_interleaving` ซึ่งมี 2 parameters นั่นคือ list `list1` และ `list2` จากนั้น function `list_interleaving` จะ return list ที่มีการนำข้อมูลมารวมกันแบบไขว้ เช่น

เมื่อนำ `list1=[1, 2, 3]` และ `list2=[-7, -6, -5]` มารวมกันแบบไขว้ จะได้ผลลัพธ์ เป็น `list=[1, -7, 2, -6, 3, -5]`

**หมายเหตุ:**  สามารถสมมติได้ว่าผู้ใช้จะ input ตัวเลขจำนวนเต็มบวกเท่านั้นสำหรับ `n` 

<hr>

**ตัวอย่างที่ 1:**
**Input:** `n1 = 2`, `n2 = 2`, `list1 = [0, 1]`และ `list2 = ['w', 'x']`
```
2
2
0
1
w
x
```
**Expected output:** โปรแกรมจะแสดงค่า list ใหม่ ที่ถูก return จาก function `list_interleaving` ดังต่อไปนี้
```
['0', 'w', '1', 'x']
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n1 = 4`, `n2 = 2`, `list1 = [0, 1, 2, 3]`และ `list2 = ['w', 'x']`
```
4
2
0
1
2
3
w
x
```
**Expected output:** โปรแกรมจะแสดงค่า list ใหม่ ที่ถูก return จาก function `list_interleaving` ดังต่อไปนี้
```
['0', 'w', '1', 'x', '2', '3']
```

<hr>

**ตัวอย่างที่ 3:**
**Input:** `n1 = 2`, `n2 = 4`, `list1 = [0, 1]`และ `list2 = ['w', 'x','y', 'z']`
```
2
4
0
1
w
x
y
z
```
**Expected output:** โปรแกรมจะแสดงค่า list ใหม่ ที่ถูก return จาก function `list_interleaving` ดังต่อไปนี้
```
['0', 'w', '1', 'x', 'y', 'z']
```