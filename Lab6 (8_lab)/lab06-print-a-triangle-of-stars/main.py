'''
lab06-print-a-triangle-of-stars
'''

# YOUR CODE HERE
m = int(input())
space = '-'
star = '*'

for row in range(m):
    line = space * (m - row - 1)  # print space font
    line += star * (2 * row + 1)  # print star
    line += space * (m - row - 1)  # print space back
    print(line)
print()
