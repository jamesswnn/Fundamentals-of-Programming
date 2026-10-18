## Create Tuple/Dictionary 
จงเขียนโปรแกรมซึ่งใช้ **loop** เป็นจำนวน `num` รอบ 
โดยในแต่ละรอบโปรแกรมจะรับข้อมูล 3 ชนิดได้แก่

1) `firstname` ชื่อ
2) `lastname` นามสกุล
3) `score` คะแนนของนักเรียน 

โดยโปรแกรมจะเก็บ (`firstname`, `lastname`) เป็น tuple และสร้าง dictionary `student_dict` โดยจะใช้ tuple (`firstname`, `lastname`) เป็น key และ `score` คะแนนของนักเรียน เป็น value  

จากนั้นโปรแกรมจะคำนวณและแสดงผลดังต่อไปนี้

* print รายชื่อของนักเรียนที่ได้คะแนนมากที่สุดดังนี้ Firstname: xxx, Last name: xxx

**หมายเหตุ:** 
นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input `score` คะแนนของนักเรียนเป็นจำนวนที่มากกว่าหรือเท่ากับ 0 เท่านั้น

นักศึกษาสามารถสมมติได้ว่ามีนักเรียนที่ได้คะแนนมากที่สุดแค่ 1 คน

<hr>

**ตัวอย่างที่ 1:**
**Input:** `num = 3` 
```
3
Kitty
Tang
10.0
Mickey
Mouse
20.0
Bad
Boy
5.0
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Mickey, Last name: Mouse
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `num = 2` 
```
2
Liga
Kick
50.0
Tiger
Sugar
20.0
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Liga, Last name: Kick
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `num = 5` 
```
5
Davika
Hoorne
100
Mario
Maurer
70
Araya
Hargate
80
Ton
Arch
90
Fern
Fern
50
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Davika, Last name: Hoorne
```
<hr>