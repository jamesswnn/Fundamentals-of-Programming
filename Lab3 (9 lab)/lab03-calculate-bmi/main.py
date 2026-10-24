'''
lab03-calculate-bmi
'''

# YOUR CODE HERE
weight = float(input())
height = float(input())

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")