'''
lab03-condition-of-x
'''

# YOUR CODE HERE
x = int(input())

if x != 0:
    print("x is positive")
else:
    print("x is not positive")

if x % 3 == 0 and x % 7 == 0:
    print("x is divisible by 3 and 7")
else:
    print("x is not divisible by 3 and 7")

if x % 10 == 1:
    print("x is ending with 1")
else:
    print("x is not ending with 1")
