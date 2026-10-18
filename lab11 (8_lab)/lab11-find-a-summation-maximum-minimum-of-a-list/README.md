## Find a Summation, Maximum, Minimum of a List

จงเขียนโปรแกรมที่ประกอบไปด้วย 2 functions
ได้แก่ `summation` และ `find_min_max`

โดย function `summation` จะรับ list ของตัวเลขเป็นจำนวน `n` ตัว มาทั้งสิ้น 2 lists ได้แก่ `lst1, lst2` และ return list ชื่อว่า `updated_list` ขนาด `n` ที่เกิดจากการผลรวมของ `lst1` และ `lst2` 

จากนั้น `updated_list` ซึ่งเป็นผลลัพธ์ของ function `summation` จะถูกใช้เป็น input ของ function `find_min_max` ซึ่งจะคำนวณหาค่าน้อยสุดและมากสุดใน list และ return ค่าน้อยสุดและมากสุดตามลำดับ

โปรแกรมจะเริ่มจากการรับค่า `n`, `lst1`, และ `lst2` 
จากนั้น โปรแกรมจะเรียก function `summation` และ function `find_min_max` ตามลำดับ และแสดงผลลัพธ์

**หมายเหตุ:** ถ้า นศ ไม่ได้ใช้ `summation` function และ `find_min_max` function เพื่อการคำนวณจะไม่ได้คะแนนจากข้อนี้ 

**ตัวอย่างที่ 1:**
**Input:** `n=3, lst1=[1,2,3], lst2=[4,5,6]`  
```
3
1
2
3
4
5
6
```
**Expected output:** โปรแกรมจะแสดงค่า output ของ function `summation` (updated_list) และ output ของ function `find_min_max` ดังต่อไปนี้
```
[5, 7, 9]
(5, 9)
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=2, lst1=[4,6], lst2=[6,4]`  
```
2
4
6
6
4
```
**Expected output:** โปรแกรมจะแสดงค่า output ของ function `summation` (updated_list) และ output ของ function `find_min_max` ดังต่อไปนี้
```
[10, 10]
(10, 10)
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n=5, lst1=[9,8,7,6,5], lst2=[1,1,1,1,1]`  
```
5
9
8
7
6
5
1
1
1
1
1
```
**Expected output:** โปรแกรมจะแสดงค่า output ของ function `summation` (updated_list) และ output ของ function `find_min_max` ดังต่อไปนี้
```
[10, 9, 8, 7, 6]
(6, 10)
```
<hr>