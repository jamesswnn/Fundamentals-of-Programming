'''
lab10-odd-and-even-dictionary
'''

set = {}

n = int(input())
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        set[num] = "even"
    else:
        set[num] = "odd"
print(set)
