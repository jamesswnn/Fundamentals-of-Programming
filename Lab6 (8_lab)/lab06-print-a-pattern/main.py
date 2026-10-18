'''
lab06-print-a-pattern
'''

# YOUR CODE HERE
star = '*'
space = '-'

while True:
    n = int(input())
    if n > 1 and n % 2 != 0:
        break

for x in range(n):
    for y in range(n):
        if y == 0 or y == n - 1 or y == x or y == n - x - 1:
            print(star, end=' ')
        else:
            print(space, end=' ')
    print()
