'''
lab11-find-a-summation-maximum-minimum-of-a-list
'''

# YOUR CODE HERE
n = int(input())
list1 = []
list2 = []

def summation():
    update_list = []
    for sums in range(n):
        update_list.append(list1[sums] + list2[sums])
    return update_list

def find_min_max(update_list):
    minVal = min(update_list)
    maxVal = max(update_list)
    return (minVal, maxVal)

for i in range(n):
    st1 = int(input())
    list1.append(st1)

for j in range(n):
    st2 = int(input())
    list2.append(st2)

updated_list = summation()
print(updated_list)
print(find_min_max(updated_list))



