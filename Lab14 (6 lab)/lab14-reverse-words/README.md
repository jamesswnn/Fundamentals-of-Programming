
# Reverse Words in a Sentence

จงเขียนโปรแกรมที่สามารถกลับลำดับของคำในประโยคภาษาอังกฤษได้

ให้ถือว่า **คำถูกแบ่งโดยเว้นวรรค** (space `' '`)

**ตัวอย่างข้อความ**  
```

This is a book

```

โปรแกรมจะแสดงผลลัพธ์ดังนี้  
```

book a is This

```

**Hint**  

- สามารถใช้ฟังก์ชัน `.split()` เพื่อแยกคำออกจากกัน  
- และใช้ `.join()` เพื่อรวมคำกลับมาเป็นประโยค

<hr>

**ตัวอย่างที่ 1:**  
**Input:**  
```

Hello World

```
**Expected output:**  
```

World Hello

```

<hr>

**ตัวอย่างที่ 2:**  
**Input:**  
```

Python Programming Language

```
**Expected output:**  
```

Language Programming Python

```
