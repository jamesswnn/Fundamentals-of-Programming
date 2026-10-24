'''
lab12-remove-negative-numbers-from-the-list
'''

n = int(input())
nums_list = []
# ----loop to get the data for the list----#
for _ in range(n):
    list_input = int(input())
    nums_list.append(list_input)

# ----print and call the function----#
result = list(filter(lambda nums_list : nums_list >= 0, nums_list)) 
print(result)