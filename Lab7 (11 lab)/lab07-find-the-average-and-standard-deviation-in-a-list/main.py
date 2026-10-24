'''
lab07-find-the-average-and-standard-deviation-in-a-list
'''
# YOUR CODE HERE
import math

num = []

while True:
    num_input = input()
    if num_input == "q":
        break
    else:
        num.append(num_input)

# หาaverage
total = 0
for i in range(len(num)):
    total = total + float(num[i])
average = total / len(num)

# หาผลรวมการเบี่ยงเบนของข้อมูลทั้งหมด
ALL_stand_devi = 0
for i in num:
    sigma = (float(i) - float(average)) ** 2
    ALL_stand_devi += sigma

# หาStandard deviation(final)
S = math.sqrt(ALL_stand_devi / (len(num) - 1))

print(f"{round(average, 2)} {round(S, 2)}")


