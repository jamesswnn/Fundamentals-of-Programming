'''
lab06-print-fibonacci-sequence
'''


# YOUR CODE HERE
x = int(input())

a = 0
b = 1

for i in range(x):
    print(a, end=" ")
    if (i + 1) % 5 == 0:
        print()
    c = a + b
    a = b
    b = c

if x % 5 != 0:
    print()
