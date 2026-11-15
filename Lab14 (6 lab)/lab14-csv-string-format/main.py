#lab14-csv-string-format

student = input()
student = student.split(",")

firstname = student[0]
lastname = student[1]
age = student[2]
gender = student[3]

if age.isdecimal():
    print(f"{lastname}, {firstname} is a {gender} student and is {age} years old.")
else:
    print("invalid input")


