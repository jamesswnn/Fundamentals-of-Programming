'''
lab06-even-numbers-and-sum
'''

# YOUR CODE HERE
n = int(input())

while True:
    if n >= 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()

        sum = (n * (n + 1)) // 2
        print(f"Sum: {sum}")
    else:
        print("n must be a positive integer")
        break
