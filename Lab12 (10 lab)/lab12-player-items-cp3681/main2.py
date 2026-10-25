#dict กิจกรรม: คะแนน เก็บว่ากิจกรรมแต่ละชนิดให้คะแนนเท่าไร
#dict นักเรียน → เซ็ตของกิจกรรม เก็บว่านักเรียนแต่ละคนเข้าร่วมกิจกรรมอะไรบ้าง

P = int(input()) #จำนวนนักเรียน
I = int(input()) #จำนวนกิจกรรม ex. sport ,5
A = int(input()) #จำนวนเข้ากิจกรรมทั้งหมด ex. นายเอ ,sport = นายเอมี 5

students = []
students_dict = dict()

#สร้างdict เก็บkey เป็นชื่อนร และ value ให้เป็นsetว่างก่อน
for _ in range(P):
    student_input = str(input())
    students.append(student_input)
    students_dict[student_input] = set()

#สร้างdict เก็บkeyเป็นชื่อกิจกรรม value เป็น คะแนนแต่ละกิจกรรม
activity_scores = dict()
for _ in range(I):
    activity_name = str(input())
    activity_score = int(input())
    activity_scores[activity_name] = activity_score
    
#เพิ่มกิจกรรมใส่นักเรียนทีละคน
for _ in range(A):
    student_input = str(input())
    activity_input = str(input())
    students_dict[student_input].add(activity_input)

#คิดคะแนนรวมแต่ละคน
for student in students:
    total = 0
    
    for activity in students_dict[student]:
        total += activity_scores[activity]
        
    print(student, total)
    
    
