## Create List of Dictionary

จงเขียนโปรแกรมเพื่อเก็บข้อมูลสินค้าที่ผู้บริโภคกดเพิ่มลงในตะกร้าสินค้า โดยมีลักษณะโครงสร้างดังต่อไปนี้

Shopping Cart [List]

    Item {Dictionary}
        name
        quantity
        price
    Item {Dictionary}
        name
        quantity
        price


ซึ่งโปรแกรมจะมี list ที่ชื่อ `shopping_list` ไว้เก็บข้อมูลสินค้าจำนวน `n` ชนิด 

โดยสินค้าแต่ละตัวจะมีโครงสร้างเป็น dictionary ประกอบไปด้วย 3 keys ได้แก่  `name` , `quantity` , `price` 

จงเขียนโปรแกรมที่รับจำนวนสินค้า `n` ชนิด จากนั้นใช้ **loop** รับข้อมูลของสินค้าแต่ละชนิด (`name` , `quantity` , `price`) เพื่อสร้าง dictionary ของสินค้าชนิดนั้นๆ
จากนั้น dictionary แต่ละตัวจะถูกเก็บเข้าไปใน   `shopping_list` list

เมื่อได้ `shopping_list` list ที่เก็บ dictionary ของสินค้าแต่ละชนิดแล้วโปรแกรมจะคำนวณและแสดงผลดังต่อไปนี้

* print `shopping_list` list
* print ยอดราคารวมโดยคำนวนจาก `quantity` * `price` ของทุกสินค้า
และแสดงผลลัพธ์ด้วยทศนิยม 1 ตำแหน่ง

<hr>

**ตัวอย่างที่ 1:**
**Input:** `n=3` 
```
3
a
1
2
b
3
4
c
5
6
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 1, 'price': 2.0}, {'name': 'b', 'quantity': 3, 'price': 4.0}, {'name': 'c', 'quantity': 5, 'price': 6.0}]
44.0
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=2` 
```
2
a
1
2
b
3
4
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 1, 'price': 2.0}, {'name': 'b', 'quantity': 3, 'price': 4.0}]
14.0
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n=1` 
```
1
a
5
5
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 5, 'price': 5.0}]
25.0
```
<hr>

