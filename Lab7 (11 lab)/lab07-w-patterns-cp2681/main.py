'''
lab07-w-patterns-cp2681
'''

# YOUR CODE GOES HERE
zigs = int(input())
height = int(input())

k = (2 * height) - 2  # ระยะห่างระหว่างยอด

for i in range(height):
    for j in range((zigs * k) + 1):

        if j % k == i or (j % k == k - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()


