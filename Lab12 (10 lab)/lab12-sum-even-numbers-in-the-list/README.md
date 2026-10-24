## Sum Even Numbers in the List

จงเขียนโปรแกรมที่รับตัวเลข `n` จำนวน มาเก็บไว้ใน list `nums_list` โดยใช้ **loop**  

โปรแกรมจะต้องมี function `sum_even_values` ซึ่งมี 1 parameter นั่นคือ list `nums_list` และ return ผลรวมของจำนวนคู่ใน list `nums_list`

**หมายเหตุ:** สามารถสมมติได้ว่า `n` เป็น ตัวเลขจำนวนเต็มบวกเท่านั้น และ input สำหรับ `nums_list` เป็นตัวเลขเท่านั้น

<hr>

**ตัวอย่างที่ 1:**
**Input:** `n = 3` และ `nums_list=[2, 2, 2]` 
```
3
2
2
2
```
**Expected output:** โปรแกรมจะแสดงค่าผลรวมของจำนวนคู่ใน list `nums_list` ดังนี้
```
6
```

<hr>

**ตัวอย่างที่ 2:**
**Input:** `n = 6` และ `nums_list = [1,2,3,4,5,6]` 
```
6
1
2
3
4
5
6
```
**Expected output:** โปรแกรมจะแสดงค่าผลรวมของจำนวนคู่ใน list `nums_list` ดังนี้
```
12
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n = 4` และ `nums_list = [-2,-4,2,1]` 
```
4
-2
-4
2
1
```
**Expected output:** โปรแกรมจะแสดงค่าผลรวมของจำนวนคู่ใน list `nums_list` ดังนี้
```
-4
```