'''
lab10-decluttering-files
'''

num1 = int(input())
folder_1 = []

for i in range(num1):
    folder_1_input = input()
    folder_1.append(folder_1_input)

folder_1 = set(folder_1)

num2 = int(input())
folder_2 = []

for j in range(num2):
    folder_2_input = input()
    folder_2.append(folder_2_input)

folder_2 = set(folder_2)

print(len(folder_1 | folder_2))
print(len(folder_1 & folder_2))

if len(folder_1 & folder_2) == 0:
    print("No duplicated found...")
else:
    print(sorted(folder_1 & folder_2))
