## Even Numbers and Their Sum

จงเขียนโปรแกรมที่รับตัวเลขจำนวนเต็ม `n` จากผู้ใช้ โดยโปรแกรมจะต้องตรวจสอบก่อนว่า `n` เป็นจำนวนเต็มบวก (positive integer) หรือไม่

- ถ้า `n` **ไม่ใช่** จำนวนเต็มบวก (เช่น `n<=0`) ให้แสดงข้อความ `n must be a positive integer` แล้วจบโปรแกรมทันที
- ถ้า `n` เป็นจำนวนเต็มบวก ให้วนลูปตั้งแต่ `1` ถึง `n` เพื่อ:
  1. แสดงเฉพาะ**เลขคู่ (even numbers)** ที่อยู่ในช่วง `1` ถึง `n`
  2. หาผลรวม (summation) ของตัวเลขทั้งหมดตั้งแต่ `1` ถึง `n` แล้วแสดงผลเมื่อจบลูป

**หมายเหตุ:** ผลรวม (summation) ในที่นี้คือผลรวมของ**ทุกจำนวนเต็ม** ตั้งแต่ `1` ถึง `n` (ไม่ใช่ผลรวมเฉพาะเลขคู่)
<hr>

**ตัวอย่างที่ 1:**
**Input:** `n=6`
```
6
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ดังต่อไปนี้
```
2 4 6 
Sum: 21
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=-3`
```
-3
```
**Expected output:** เนื่องจาก `n` ไม่ใช่จำนวนเต็มบวก โปรแกรมจะแสดงข้อความและจบการทำงานทันที
```
n must be a positive integer
```
<hr>

## Test Cases

**Test Case 1: `n=1`**
Input:
```
1
```
Expected output:
```

Sum: 1
```
*(ไม่มีเลขคู่ในช่วงนี้ จึงมีเพียงบรรทัดว่างตามด้วยผลรวม)*
<hr>

**Test Case 2: `n=2`**
Input:
```
2
```
Expected output:
```
2 
Sum: 3
```
<hr>

**Test Case 3: `n=10`**
Input:
```
10
```
Expected output:
```
2 4 6 8 10 
Sum: 55
```
<hr>

**Test Case 4: `n=0`**
Input:
```
0
```
Expected output:
```
n must be a positive integer
```
<hr>

**Test Case 5: `n=-5`**
Input:
```
-5
```
Expected output:
```
n must be a positive integer
```
<hr>
