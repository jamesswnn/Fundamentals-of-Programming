'''
lab12-func-search-frequency
'''

# YOUR CODE HERE

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''
n = int(input())
nums_list = []

for i in range(n):
    list_input = int(input())
    nums_list.append(list_input)

search = int(input())

def frequency(nums_list, search):
    count_same_numbers = 0

    for i in nums_list:
        if i == search:
            count_same_numbers += 1
        else:
            continue

    return count_same_numbers

print(frequency(nums_list, search))