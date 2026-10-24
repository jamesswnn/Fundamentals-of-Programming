'''
lab05-series-of-numbers
'''

# YOUR CODE HERE
x = int(input())
y = int(input())
current = ''

for i in range(y):
    current = current + str(x)

    if i < y - 1:
        print(current, end=',')
    else:
        print(current, end='')
