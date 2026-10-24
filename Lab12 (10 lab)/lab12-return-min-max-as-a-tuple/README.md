## Return Min Max as a Tuple
จงเขียนโปรแกรมที่รับตัวเลข `n` จำนวน มาเก็บไว้ใน list `nums_list` โดยใช้ **loop** 

จากนั้นโปรแกรมจะเรียกใช้ function `extreme` ซึ่งมี 1 parameter นั่นคือ list `nums_list` ซึ่งจะ return tuple ของค่าน้อยที่สุดและค่าที่มากที่สุดใน `nums_list` 

ใน function `extreme` สามารถใช้ built-in function `min` และ `max` เพื่อให้ค่าที่น้อยที่สุดและมากที่สุดตามลำดับ

**หมายเหตุ:** สามารถสมมติได้ว่า `n` ้เป็นตัวเลขจำนวนเต็มบวกเท่านั้นสำหรับ และค่า input ใน `nums_list` จะเป็นตัวเลขเท่านั้น

<hr>

**ตัวอย่างที่ 1:**
**Input:** `n = 6` และ `nums_list=[1, 2,
3, 4, 5, 6]` 
```
6
1
2
3
4
5
6
```
**Expected output:** โปรแกรมจะแสดงค่าใน tuple ที่ถูก return จาก function `extreme` ดังต่อไปนี้
```
(1, 6)
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n = 5` และ `nums_list = [-1, -3, -6, -9, -4]` 
```
5
-1
-3
-6
-9
-4
```
**Expected output:** โปรแกรมจะแสดงค่าใน tuple ที่ถูก return จาก function `extreme` ดังต่อไปนี้
```
(-9, -1)
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n = 3` และ `nums_list = [5, -3, 8]` 
```
3
5
-3
8
```
**Expected output:** โปรแกรมจะแสดงค่าใน tuple ที่ถูก return จาก function `extreme` ดังต่อไปนี้
```
(-3, 8)
```