'''
/**
USERID: 6987012
PASSWORD: 9bd0a2
EXERCISEID: itds120-lab03-grade-calculation
 */
'''

# YOUR CODE HERE

lab = float(input())
assignment = float(input())
quiz = float(input())
checkpoint = float(input())
project = float(input())

score = (lab / 12) * 10 + (assignment / 12) * 10 + (quiz / 12) * 10 + (checkpoint / 80) * 50 + (project / 100) * 20

if score >= 85:
    print("Grade: A")
elif score >= 80:
    print("Grade: B+")
elif score >= 75:
    print("Grade: B")
elif score >= 70:
    print("Grade: C+")
elif score >= 65:
    print("Grade: C")
elif score >= 60:
    print("Grade: D+")
elif score >= 50: 
    print("Grade: D")
else:
    print("Grade: F")