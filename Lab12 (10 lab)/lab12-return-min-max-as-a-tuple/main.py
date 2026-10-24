'''
return-min-max-as-a-tuple
'''

n = int(input())
nums_list = []
# ----loop to get the data for the list----#
for _ in range(n):
    list_input = int(input())
    nums_list.append(list_input)

# ----print and call the function----#


def extreme(nums_list):
    return (min(nums_list), max(nums_list))

print(extreme(nums_list))