## Combine Words
โปรแกรมต่อไปนี้มี code ให้บางส่วนแล้ว นักศึกษาจงเติม code ใน function `combine_words` เพื่อให้โปรแกรมสมบูรณ์

โปรแกรมจะรับ 3 inputs ดังต่อไปนี้

&nbsp; &nbsp; input_text = input()

&nbsp; &nbsp; position_text = input()

&nbsp; &nbsp; extra_text = input()

จากนั้นโปรแกรมจะเรียก function `combine_words` ซึ่งมี parameter `word` และ `**kwargs` โดยรับ `input_text` และ dictionary ที่มี key-value pairs ดังนี้ `position = position_text, extra=extra_text`

* ถ้า `position_text` มีค่าเป็น `prefix`, function `combine_words`จะ return `extra_text` ตามด้วย `word`

* ถ้า `position_text` มีค่าเป็น `suffix`, function `combine_words`จะ return `word` ตามด้วย `extra_text` 

* ถ้า `position_text` มีค่าเป็นอย่างอื่นนอกเหนือจาก `prefix`  หรือ `suffix`, function `combine_words`จะ return `word`


**หมายเหตุ:** 
* นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input string เท่านั้น

<hr>

**ตัวอย่างที่ 1:**
**Input:**   `input_text = child`, `position_text = no` และ `extra_text = no`
```
child
no
no
```
**Expected output:** เนื่องจาก `position_text = no` function `combine_words`จะ return `word`
```
child
```

<hr>

**ตัวอย่างที่ 2:**
**Input:**   `input_text = child`, `position_text = prefix` และ `extra_text = man`
```
child
prefix
man
```
**Expected output:** เนื่องจาก `position_text = prefix` function `combine_words`จะ return `extra_text` ตามด้วย `word`
```
manchild
```

<hr>

**ตัวอย่างที่ 3:**
**Input:**   `input_text = child`, `position_text = suffix` และ `extra_text = ish`
```
child
suffix
ish
```
**Expected output:** เนื่องจาก `position_text = suffix` function `combine_words` จะ return `word` ตามด้วย `extra_text` 
```
childish
```

**ตัวอย่างที่ 4:**
**Input:**   `input_text = work`, `position_text = prefix` และ `extra_text = home`
```
work
prefix
home
```
**Expected output:** เนื่องจาก `position_text = prefix` function `combine_words` จะ return `extra_text` ตามด้วย `word`
```
homework
```