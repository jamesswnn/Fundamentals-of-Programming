'''
lab06-print-coordinate-matrix
'''

# YOUR CODE HERE
n = int(input())
x = int(input())
y = int(input())

for row in range(0, n, 1):
    for col in range(0, n, 1):
        print(f"({row},{col})", end=" ")
        if row == x and col == y:
            break
    if row == x and col == y:
        break

    print()
