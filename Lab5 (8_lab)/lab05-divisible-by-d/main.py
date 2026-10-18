'''
lab05-divisible-by-d
'''

# YOUR CODE HERE
x = int(input())
y = int(input())
d = int(input())

result = ''
count = 0

for i in range(x, y + 1):
    if i % d == 0:
        result += str(i) + ' '
        count += 1

print(f"{result}count={count}")
