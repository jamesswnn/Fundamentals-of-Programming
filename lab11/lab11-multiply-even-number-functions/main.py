'''
lab11-multiply-even-number-functions
'''

# YOUR CODE HERE

def multiply_even_numbers(list):
    count_even_numbers = 0
    output = 1

    for elem in list:
        if elem % 2 == 0:
            output = output*elem
            count_even_numbers = count_even_numbers + 1

    if count_even_numbers == 0:
        return -1
    else:
        return output

n = int(input())
list_lst = []

for i in range(n):
    num = int(input())
    list_lst.append(num)

print(multiply_even_numbers(list_lst))