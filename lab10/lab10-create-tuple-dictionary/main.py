'''
lab10-create-tuple-dictionary
'''

num = int(input())
student_dict = dict()

for i in range(num):
    firstname = str(input())
    lastname = str(input())
    score = float(input())

    student_dict[(firstname, lastname)] = score

max_score = -1
max_student = ()

for student, score in student_dict.items():
    if score > max_score:
        max_score = score
        max_student = student

print(f"Firstname: {max_student[0]}, Last name: {max_student[1]}")