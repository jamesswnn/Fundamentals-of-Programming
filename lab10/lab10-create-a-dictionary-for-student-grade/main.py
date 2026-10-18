'''
lab10-create-a-dictionary-for-student-grade
'''

name = input()
grade = input()

student = {'name': name, 'grade': grade}

if grade == 'a':
    student['GRADE'] = student.pop('grade')

print(student)
