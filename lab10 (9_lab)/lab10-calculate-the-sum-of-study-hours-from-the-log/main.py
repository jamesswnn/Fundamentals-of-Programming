'''
lab10-calculate-the-sum-of-study-hours-from-the-log
'''
num = int(input())
key_list = []  # string
value_list = []  # float

study_hours = dict()

for i in range(num):
    key_input = str(input())
    value_input = float(input())

    key_list.append(key_input)
    value_list.append(value_input)

for j in range(num):
    study_hours[key_list[j]] = value_list[j]

total = 0

for value in study_hours.values() :
    total += value

print(study_hours)
print(round(total, 1))


