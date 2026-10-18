'''
lab07-list-insert-and-update
'''
# YOUR CODE HERE
list_A = []

while True:
    if len(list_A) == 5:
        break
    else:
        input_loop = float(input())
        list_A.append(input_loop)

x = float(input())
for i in range(len(list_A)):
    if list_A[i] > x:
        list_A[i] = 'g'
    elif list_A[i] < x:
        list_A[i] = 's'
    else:
        list_A[i] = 'e'


print(list_A)


