'''
lab07-sum-first-and-last-k-numbers-in-a-list
'''
# YOUR CODE HERE
k = int(input())

list_A = []
a_input = input()

while str(a_input) != "q":
    list_A.append(float(a_input))
    a_input = input()

if len(list_A) < k:
    print("Invalid")
else:
    sum_k_first = 0.0
    sum_k_last = 0.0

    for i in range(0, k, 1):
        sum_k_first += list_A[i]
        sum_k_last += list_A[len(list_A) - 1 - i]

    all_sum = sum_k_first + sum_k_last

    print(all_sum)


