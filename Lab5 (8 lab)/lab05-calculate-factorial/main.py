'''
lab05-calculate-factorial
'''

# YOUR CODE HERE
x = int(input())
result = 1

if x == 1 or x == 0:
    print("1")
else:
    for i in range(x, 1, -1):
        print(f"{i}*", end="")
        result *= i

    print(f"1={result}")
