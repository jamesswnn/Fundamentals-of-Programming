## Another List Manipulation

โปรแกรมต่อไปนี้มี code ให้บางส่วนแล้ว นักศึกษาจงเติม code ใน function `list_manipulation` เพื่อให้โปรแกรมสมบูรณ์

โดยหน้าที่ของ function `list_manipulation` คือการเปลี่ยนแปลงค่าของตัวเลขในลิสต์ และ filter ค่าเหล่านั้น **ก่อน/หลัง** ของการเปลี่ยนแปลงค่า

function `list_manipulation` มี parameter ทั้งหมด 4 ตัว ได้แก่:
- func (lambda function) -> function ที่ใช้ในการเปลี่ยนแปลงค่าของ `data`
- data (list จำนวนเต็ม)-> list ที่จะถูกดำเนินการเปลี่ยนแปลงค่า
- param (ตัวเลขจำนวนเต็ม) -> ตัวแปรที่จะถูกใช้ร่วมกับ `data` ใน `func`
- **kwargv -> วิธีการ filter ข้อมูลใน `data`
    - when -> ลำดับการ filter ข้อมูล
        - when = pre -> filter ข้อมูล **ก่อน** เรียกใช้ `func`
        - when = post -> filter ข้อมูล **หลัง** เรียกใช้ `func`
    - how -> วิธีการ filter ข้อมูล
        - how = pos -> เลือกเฉพาะจำนวนเต็มบวก
        - how = neg -> เลือกเฉพาะจำนวนเต็มลบ

Note: 
- ตัวแปร param มีค่า default เป็น 2
- หากไม่มีการระบุ when และ how ให้ดำเนินการแก้ไขข้อมูลในลิสต์โดยไม่ต้อง filter ข้อมูล

<hr>

**ตัวอย่างที่ 1:**
**Input:**
```
1
1 2 -3 4 -5
2
- -
```
**Expected output:** 
```
[3, 4, -1, 6, -3]
```
<hr>

**ตัวอย่างที่ 2:**
**Input:**
```
1
1 2 -3 4 -5
5
pre neg
```
**Expected output:** 
```
[2, 0]
```
<hr>

**ตัวอย่างที่ 3:**
**Input:**
```
2
1 2 -3 4 -5 -6 7 8 9 10
5
post pos
```
**Expected output:** 
```
[2, 3, 4, 5]
```
<hr>
