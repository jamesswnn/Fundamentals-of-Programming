'''
lab12-sum-even-numbers-in-the-list
'''

n = int(input())
nums_list = []

# ----loop to get the data for the list----#
for _ in range(n):
    list_input = int(input())
    nums_list.append(list_input)

# ----print and call the function----#


def sum_even_values(nums_list):
    total = 0

    for i in nums_list:
        if i % 2 == 0:
            total = total + i

    return total


print(sum_even_values(nums_list))