'''
lab12-list-interleaving
'''

# YOUR CODE HERE

n1 = int(input())
n2 = int(input())

list1 = []
list2 = []

for _ in range(n1):
    list1_input = input()
    list1.append(list1_input)

for _ in range(n2):
    list2_input = input()
    list2.append(list2_input)


def list_interleaving(list1, list2):
    result = []

    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            result.append(list1[i])

        if i < len(list2):
            result.append(list2[i])

    return result


print(list_interleaving(list1, list2))