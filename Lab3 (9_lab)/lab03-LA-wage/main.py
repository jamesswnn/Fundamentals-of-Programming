'''
lab03-LA-wage
'''

# YOUR CODE HERE
hr = int(input())
hr_wage = 0

if hr <= 40 :
    hr_wage = hr * 50
else :
    hr_wage += 2000
    hr_wage += (hr - 40) * 75

print(hr_wage)